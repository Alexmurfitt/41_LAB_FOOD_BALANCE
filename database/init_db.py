from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base, NutritionalRequirement, Food
import pandas as pd
import os

# Configura tu URI de conexión a PostgreSQL (ajustar según .env o sistema local)
# Ejemplo: postgresql://usuario:contraseña@localhost:5432/nutrisystem
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://usuario:contraseña@localhost:5432/nutrisystem")

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# Crear todas las tablas definidas en models.py
Base.metadata.drop_all(engine)  # ❗ Elimina todas las tablas anteriores (cuidado en producción)
Base.metadata.create_all(engine)

# Cargar y poblar tabla de requerimientos nutricionales
idr_df = pd.read_csv("nutrisystem_data/idr_values.csv")
for _, row in idr_df.iterrows():
    req = NutritionalRequirement(
        nutrient=row["Nutrient"],
        unit=row["Unit"],
        value=row["Value"]
    )
    session.add(req)

# Cargar y poblar tabla de alimentos
food_df = pd.read_csv("nutrisystem_data/food_database.csv")
for _, row in food_df.iterrows():
    food = Food(
        name=row["Name"],
        group=row["Group"],
        kcal=row["Kcal"],
        protein=row["Protein"],
        fat=row["Fat"],
        carbs=row["Carbs"],
        fiber=row["Fiber"],
        iron=row["Iron"],
        calcium=row["Calcium"],
        vitamin_c=row["Vitamin_C"],
        vitamin_d=row["Vitamin_D"]
    )
    session.add(food)

# Confirmar los cambios
session.commit()
session.close()

print("✅ Base de datos creada y poblada exitosamente.")
