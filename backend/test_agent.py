from agents.agent import DataPilotAgent

agent = DataPilotAgent()

questions = [

    "Top 10 customers by sales",

    "Forecast next month's sales",

    "Show anomalies",

    "What does the uploaded report say about revenue?"
]

for q in questions:

    print("=" * 60)

    print(q)

    result = agent.run(q)

    print()

    print(result["tool"])