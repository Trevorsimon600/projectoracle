def score_task(task: dict) -> float:
    # Simple scoring: importance & urgency & strategic (here 'priority' if present) minus effort
    importance = task.get("importance", 5)
    urgency = task.get("urgency", 5)
    effort = task.get("effort", 5)
    priority = task.get("priority", task.get("priority", 5))
    score = (importance * 2) + (urgency * 1.5) + (priority) - (effort * 1)
    return score
