from random import choice  # magic 8 ball

choices = [
    'It is certain (Бесспорно)',
    'It is decidedly so (Предрешено)',
    'Without a doubt (Никаких сомнений)',
    'Yes — definitely (Определённо да)',
    'You may rely on it (Можешь быть уверен в этом)',
    'As I see it, yes (Мне кажется — «да»)',
    'Most likely (Вероятнее всего)',
    'Outlook good (Хорошие перспективы)',
    'Signs point to yes (Знаки говорят — «да»)',
    'Yes (Да)',
    'Reply hazy, try again (Пока не ясно, попробуй снова)',
    'Ask again later (Спроси позже)',
    'Better not tell you now (Лучше не рассказывать)',
    'Cannot predict now (Сейчас нельзя предсказать)',
    'Concentrate and ask again (Соберись и спроси опять)',
    'Don’t count on it (Даже не думай)',
    'My reply is no (Мой ответ — «нет»)',
    'My sources say no (По моим данным — «нет»)',
    'Outlook not so good (Перспективы не очень хорошие)',
    'Very doubtful (Весьма сомнительно)',
]

input("Ваш вопрос: ")
print(choice(choices))
