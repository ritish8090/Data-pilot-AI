from query_executor import execute_question

question = "Top 5 customers by revenue"

result = execute_question(question)

print("=" * 60)
print("QUESTION")
print(result["question"])

print("\nGENERATED SQL")
print(result["sql"])

if "error" in result:
    print("\nERROR")
    print(result["error"])
else:
    print("\nRESULT")
    print(result["data"])