from sql_generator import generate_sql

question = "Top 5 customers by revenue"

sql = generate_sql(question)

print("Question:")
print(question)

print("\nGenerated SQL:")
print(sql)