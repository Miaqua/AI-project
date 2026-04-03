def build_prompt(mode: str, user_prompt: str, code: str | None = None) -> str:
    common = (
        "Ты помощник разработчика. "
        "Отвечай структурированно, понятно и по делу. "
        "Если пользователь дал код, учитывай его в ответе."
    )

    mode_instructions = {
        "explain": "Объясни, что делает код или как решить задачу.",
        "fix": "Найди ошибки, объясни их и предложи исправленную версию.",
        "generate": "Сгенерируй рабочий пример кода по запросу пользователя.",
        "review": "Сделай краткое code review: сильные стороны, проблемы, улучшения.",
    }

    prompt = f"{common}\nРежим: {mode_instructions.get(mode, 'Помоги пользователю.')}\n\nЗапрос пользователя:\n{user_prompt}"
    if code:
        prompt += f"\n\nКод:\n```\n{code}\n```"
    return prompt
