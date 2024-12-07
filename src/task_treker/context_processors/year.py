from datetime import datetime


def year(request):
    """Добавляет переменную с текущим годом.

    Returns:
        Вщзвращает текущий год.
    """
    return {'year': datetime.now().year}

