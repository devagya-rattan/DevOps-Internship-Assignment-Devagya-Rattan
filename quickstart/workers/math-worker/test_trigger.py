from iii import trigger

result = trigger(
    "ws://43.205.212.249:49134",
    {
        "function_id": "math::add",
        "payload": {
            "a": 2,
            "b": 3
        }
    }
)

print(result)