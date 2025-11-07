# -*- coding: utf-8 -*-
import os
import sys

# Lê a variável BOT_ATIVO do Railway (ou usa "false" se não existir)
BOT_ATIVO = os.getenv("BOT_ATIVO", "false").lower()

if BOT_ATIVO != "true":
    print("🚫 Bot está desativado pelo administrador. Encerrando...")
    sys.exit(0)

import telebot
from telebot import types
import json

# --- НАСТРОЙКИ БОТА / CONFIGURAÇÕES DO BOT ---

# Вставьте сюда токен вашего бота, полученный от @BotFather
# Insira aqui o token do seu bot, obtido do @BotFather
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Укажите ID администраторов через запятую
# Especifique os IDs dos administradores, separados por vírgula
ADMIN_IDS = [7428791161, 1993108159]

# Ссылка на ваше мини-приложение
# Link para o seu mini-aplicativo
MINI_APP_URL = 'https://zenobioyenom.github.io/appmineswin/'

# Ссылка на поддержку
# Link para o suporte
SUPPORT_LINK = 'https://t.me/koalamoney3'

# Имя файла для хранения данных пользователей
# Nome do arquivo para armazenar os dados dos usuários
DB_FILE = 'users_data.json'

# --- ТЕКСТЫ БОТА (МНОГОЯЗЫЧНОСТЬ) / TEXTOS DO BOT (MULTILÍNGUE) ---
# Все тексты хранятся в словаре для удобного переключения языков
# Todos os textos são armazenados em um dicionário para facilitar a troca de idiomas
TEXTS = {
    'ru': {
        'choose_lang': "Выберите язык / Choose your language / Elige tu idioma:",
        'welcome': (
            "👋 Привет!\n"
            "Добро пожаловать в нашего уникального 🤖 бота, который связан напрямую с серверами 1win!\n\n"
            "🎯 **Что он делает?**\n"
            "Наш бот умеет предсказывать результаты игр ещё до того, как они появляются у тебя на экране. Это возможно благодаря технологии перехвата сигнала от генератора случайных чисел 🔐\n\n"
            "💻 Над проектом трудились лучшие русские программисты, вложив в него много сил и времени, чтобы ты мог:\n"
            "✅ Играть\n"
            "✅ Выигрывать\n"
            "✅ И делать это **БЕСПЛАТНО**\n\n"
            "🚫 Никаких скрытых платежей\n"
            "🚫 Никаких подписок\n"
            "🔓 Просто регистрируйся, запускай бота и наслаждайся выигрышами 💰\n\n"
            "Если будут вопросы — пиши, команда всегда на связи 🤝"
        ),
        'sync_button': "Синхронизировать бота с аккаунтом 1win🛠",
        'instruction_1': (
            "📢 **Внимание! Важные шаги для подключения бота** 🔗\n\n"
            "Для того чтобы я мог отслеживать игровые сессии и бот работал корректно, мне нужно немного данных от тебя 🙌\n\n"
            "🧾 **Что нужно сделать?**\n\n"
            "1️⃣ **Создай НОВЫЙ аккаунт** на официальном сайте по ссылке ниже\n"
            "_(обязательно новый, иначе бот не сможет подключиться!)_\n\n"
            "2️⃣ В течение 24 часов **отправь мне свой ID** (Чем раньше тем лучше)\n"
            "📩 Я подключу его к специальному коду, чтобы всё работало корректно\n\n"
            "3️⃣ Обязательно используй кнопку ниже для регистрации\n"
            "🔗 Или скопируй ссылку вручную:\n"
            "`https://1wtsks.com/v3/landing-fortune-wheel?p=gv72`\n"
            "_(если не открывается — просто вставь её в любой браузер)_\n\n"
            "4️⃣ При регистрации введи промокод:\n"
            "🎁 `MOB500RR`\n"
            "Он активирует соединение с ботом и даст тебе бонусы 💰\n\n"
            "⚠️ **Без выполнения всех шагов бот не сможет подключиться к твоему аккаунту**\n"
            "Так что не пропускай ни один пункт 🛠"
        ),
        'register_button_text': "Перейти к регистрации 🔗",
        'steps_done_button': "Все пункты выполнены 🛠",
        'instruction_2': (
            "🎉 Супер! Мы уже на финишной прямой\n"
            "Осталось совсем чуть-чуть до того момента, когда ты сможешь сам убедиться, что бот работает как часы! ⏱️🤖\n\n"
            "📌 **Сейчас мне нужно узнать твой ID** —\n"
            "это нужно, чтобы бот понимал, какие именно сессии ему нужно проверять. Без этого он не сможет подключиться к тебе правильно 🙈\n\n"
            "🧭 **Как узнать свой ID:**\n"
            "Просто нажми на кнопку в профиле (как показано на инструкции) и отправь его мне.\n"
            "Можешь:\n"
            "✅ Написать ID текстом — это самый быстрый способ\n"
            "📸 Или прислать скриншот с ID — тоже подойдёт!\n\n"
            "Жду тебя! 💌"
        ),
        'send_id_button': "Отправить мой ID и подключить его к боту🛠",
        'prompt_for_id': "Отправь свой ID или фотографию прямо в этот чат 👇",
        'id_received': (
            "Принято! 👍\n\n"
            "Все операции проводятся вручную, так как система сложная и её невозможно автоматизировать. Наша команда уже получила все данные и занимается внесением тебя в списки доступа, и как я обещал, все абсолютно бесплатно.\n\n"
            "Я могу позволить платить за вас сумму, которая требуется, а в будущем и ты сможешь использовать деньги, чтобы помогать другим😉\n\n"
            "Я напишу тебе сразу, как все будет готово!"
        ),
        'wrong_data_button': "Я отправил не те данные ⚠️",
        'change_data_prompt': "Я изменю данные аккаунта, если те были отправлены с ошибкой. Пожалуйста, отправь правильные данные.",
        'data_changed': "Изменил твои данные и сообщил об изменениях сотрудникам✍️",
        'support_button': "Обратиться в поддержку 👨‍💻",
        'access_granted': (
            "🎉 **Поздравляю! Доступ разрешён!**\n"
            "Ты успешно подключён к приложению, которое помогает узнавать результаты любой твоей игры в Mines 💣 — теперь всё под контролем! 🧠💸\n\n"
            "📌 **Немного правил, чтобы всё работало чётко:**\n"
            "Наш бот анализирует только реальные игры, проходящие в официальной системе.\n"
            "❗️**В демо-режиме бот не работает.**\n\n"
            "🔧 **Как пользоваться ботом:**\n\n"
            "1️⃣ Запусти игру, сделай ставку, но ничего не нажимай!\n"
            "2️⃣ Перейди в мини-приложение бота и нажми кнопку 'Analisar padrão' 🔍\n"
            "3️⃣ Получи список безопасных клеток ✅\n"
            "4️⃣ Повторяй ходы, которые подсказывает бот, и выводи деньги! 💰🎯\n\n"
            "⚠️ **Важно:**\n"
            "Не рискуй по наитию. Зарабатывать нужно с холодной головой и только по проверенным клеточкам 🧊🧠"
        ),
        'open_app_button': "Открыть приложение 📲",
        'access_denied': "Извините, но после проверки были выявлены причины, по которым мы не можем предоставить вам доступ к боту.",
        'access_temp_denied': (
            "🚫 **Упс! Доступ не выдан**\n"
            "К сожалению, подключение к боту прошло с ошибкой 😔\n\n"
            "📌 Пожалуйста, внимательно следуй рекомендациям нашего сотрудника, чтобы всё прошло правильно.\n"
            "Вот что он пишет:\n"
            "📝 _«{comment}»_"
        ),
        # Admin texts
        'admin_panel_title': "Панель администратора",
        'incoming_requests_button': "Входящие заявки",
        'stats_button': "Статистика",
        'status_button': "Статус бота",
        'no_pending_requests': "Новых заявок на проверку нет.",
        'request_from_user': "Заявка от пользователя ID `{user_id}`.\nПредоставленные данные:\n`{user_data}`",
        'accept_button': "✅ Принять",
        'reject_button': "❌ Отказать",
        'reject_with_comment_button': "📝 Отказать с комм.",
        'prompt_for_rejection_comment': "Введите причину отказа для пользователя ID `{user_id}`. Этот текст будет отправлен ему.",
        'request_accepted': "✅ Доступ для пользователя `{user_id}` разрешен.",
        'request_rejected': "❌ Пользователю `{user_id}` отказано в доступе.",
        'request_rejected_with_comment': "📝 Пользователю `{user_id}` отказано в доступе с комментарием.",
        'bot_status_ok': "✅ Бот работает в штатном режиме.",
        'stats_info': "📊 **Статистика:**\n\n- Принято заявок: `{accepted}`\n- Отклонено заявок: `{rejected}`\n- Ожидают проверки: `{pending}`",
    },
    'pt': {
        'choose_lang': "Escolha o seu idioma / Choose your language / Elige tu idioma:",
        'welcome': (
            "👋 Olá!\n"
            "Bem-vindo ao nosso 🤖 bot exclusivo, que está diretamente conectado aos servidores da 1win!\n\n"
            "🎯 **O que ele faz?**\n"
            "Nosso bot consegue prever os resultados dos jogos antes mesmo que eles apareçam na sua tela. Isso é possível graças a uma tecnologia que intercepta o sinal do gerador de números aleatórios 🔐\n\n"
            "💻 Os melhores programadores russos trabalharam neste projeto, investindo muito tempo e esforço para que você possa:\n"
            "✅ Jogar\n"
            "✅ Ganhar\n"
            "✅ E fazer tudo isso **GRATUITAMENTE**\n\n"
            "🚫 Sem taxas ocultas\n"
            "🚫 Sem assinaturas\n"
            "🔓 Basta se registrar, iniciar o bot e aproveitar os seus ganhos 💰\n\n"
            "Se tiver alguma dúvida, é só chamar. Nossa equipe está sempre online 🤝"
        ),
        'sync_button': "Sincronizar o bot com a conta 1win🛠",
        'instruction_1': (
            "📢 **Atenção! Passos importantes para conectar o bot** 🔗\n\n"
            "Para que eu possa rastrear suas sessões de jogo e o bot funcione corretamente, preciso de alguns dados seus 🙌\n\n"
            "🧾 **O que você precisa fazer?**\n\n"
            "1️⃣ **Crie uma NOVA conta** no site oficial usando o link abaixo\n"
            "_(é obrigatório que seja uma conta nova, caso contrário, o bot não conseguirá se conectar!)_\n\n"
            "2️⃣ Em até 24 horas, **envie-me o seu ID** (quanto antes, melhor)\n"
            "📩 Eu o conectarei a um código especial para que tudo funcione corretamente\n\n"
            "3️⃣ Use o botão abaixo para se registrar\n"
            "🔗 Ou copie o link manualmente:\n"
            "`https://1wtsks.com/v3/landing-fortune-wheel?p=gv72`\n"
            "_(se não abrir, basta colá-lo em qualquer navegador)_\n\n"
            "4️⃣ Ao se registrar, insira o código promocional:\n"
            "🎁 `MOB500RR`\n"
            "Ele ativará a conexão com o bot e lhe dará bônus 💰\n\n"
            "⚠️ **Sem seguir todos os passos, o bot não conseguirá se conectar à sua conta**\n"
            "Portanto, não pule nenhuma etapa 🛠"
        ),
        'register_button_text': "Ir para o registro 🔗",
        'steps_done_button': "Todos os passos foram concluídos 🛠",
        'instruction_2': (
            "🎉 Ótimo! Estamos quase lá\n"
            "Falta muito pouco para você ver com seus próprios olhos que o bot funciona como um relógio! ⏱️🤖\n\n"
            "📌 **Agora preciso do seu ID** —\n"
            "isso é necessário para que o bot saiba quais sessões ele precisa verificar. Sem isso, ele не сможет se conectar a você corretamente 🙈\n\n"
            "🧭 **Como encontrar o seu ID:**\n"
            "Basta clicar no botão do seu perfil (como mostrado nas instruções) e me enviar.\n"
            "Você pode:\n"
            "✅ Escrever o ID em texto — é a forma mais rápida\n"
            "📸 Ou enviar uma captura de tela com o ID — também funciona!\n\n"
            "Estou aguardando! 💌"
        ),
        'send_id_button': "Enviar meu ID e conectá-lo ao bot🛠",
        'prompt_for_id': "Envie seu ID ou uma foto diretamente neste chat 👇",
        'id_received': (
            "Recebido! 👍\n\n"
            "Todas as operações são feitas manualmente, pois o sistema é complexo e não pode ser automatizado. Nossa equipe já recebeu todos os seus dados e está trabalhando para adicioná-lo às listas de acesso. E, como prometido, tudo é totalmente gratuito.\n\n"
            "Eu posso arcar com os custos necessários por você, e no futuro, você também poderá usar o dinheiro para ajudar outras pessoas 😉\n\n"
            "Avisarei assim que tudo estiver pronto!"
        ),
        'wrong_data_button': "Eu enviei os dados errados ⚠️",
        'change_data_prompt': "Vou alterar os dados da conta se foram enviados com erro. Por favor, envie os dados corretos.",
        'data_changed': "Seus dados foram alterados e a equipe foi notificada sobre as mudanças✍️",
        'support_button': "Contatar o suporte 👨‍💻",
        'access_granted': (
            "🎉 **Parabéns! Acesso concedido!**\n"
            "Você foi conectado com sucesso ao aplicativo que ajuda a descobrir os resultados de qualquer um dos seus jogos no Mines 💣 — agora tudo está sob controle! 🧠💸\n\n"
            "📌 **Algumas regras para que tudo funcione perfeitamente:**\n"
            "Nosso bot analisa apenas jogos reais que ocorrem no sistema oficial.\n"
            "❗️**O bot não funciona no modo de demonstração.**\n\n"
            "🔧 **Como usar o bot:**\n\n"
            "1️⃣ Inicie o jogo, faça uma aposta, mas не clique em nada!\n"
            "2️⃣ Vá para o mini-aplicativo do bot e pressione o botão 'Analisar padrão' 🔍\n"
            "3️⃣ Receba a lista de células seguras ✅\n"
            "4️⃣ Repita os movimentos que o bot sugere e saque o dinheiro! 💰🎯\n\n"
            "⚠️ **Importante:**\n"
            "Não arrisque por intuição. Ganhe dinheiro com a cabeça fria e apenas nas células verificadas 🧊🧠"
        ),
        'open_app_button': "Abrir aplicativo 📲",
        'access_denied': "Desculpe, mas após a verificação, foram encontrados motivos pelos quais não podemos conceder acesso ao bot.",
        'access_temp_denied': (
            "🚫 **Oops! Acesso não concedido**\n"
            "Infelizmente, a conexão com o bot falhou 😔\n\n"
            "📌 Por favor, siga atentamente as recomendações do nosso funcionário para que tudo corra bem.\n"
            "Aqui está o que ele diz:\n"
            "📝 _«{comment}»_"
        ),
    },
    'es': {
        'choose_lang': "Elige tu idioma / Choose your language / Escolha o seu idioma:",
        'welcome': (
            "👋 ¡Hola!\n"
            "¡Bienvenido a nuestro 🤖 bot único, que está conectado directamente con los servidores de 1win!\n\n"
            "🎯 **¿Qué hace?**\n"
            "Nuestro bot puede predecir los resultados de los juegos incluso antes de que aparezcan en tu pantalla. Esto es posible gracias a una tecnología que intercepta la señal del generador de números aleatorios 🔐\n\n"
            "💻 Los mejores programadores rusos trabajaron en este proyecto, invirtiendo mucho tiempo y esfuerzo para que tú pudieras:\n"
            "✅ Jugar\n"
            "✅ Ganar\n"
            "✅ Y hacerlo **GRATIS**\n\n"
            "🚫 Sin pagos ocultos\n"
            "🚫 Sin suscripciones\n"
            "🔓 Simplemente regístrate, inicia el bot y disfruta de tus ganancias 💰\n\n"
            "Si tienes alguna pregunta, solo escríbenos. El equipo siempre está en línea 🤝"
        ),
        'sync_button': "Sincronizar el bot con la cuenta de 1win🛠",
        'instruction_1': (
            "📢 **¡Atención! Pasos importantes para conectar el bot** 🔗\n\n"
            "Para que pueda rastrear tus sesiones de juego y el bot funcione correctamente, necesito algunos datos tuyos 🙌\n\n"
            "🧾 **¿Qué necesitas hacer?**\n\n"
            "1️⃣ **Crea una NUEVA cuenta** en el sitio web oficial usando el siguiente enlace\n"
            "_(¡es obligatorio que sea nueva, de lo contrario el bot no podrá conectarse!)_\n\n"
            "2️⃣ En un plazo de 24 horas, **envíame tu ID** (cuanto antes, mejor)\n"
            "📩 Lo conectaré a un código especial para que todo funcione correctamente\n\n"
            "3️⃣ Asegúrate de usar el botón de abajo para registrarte\n"
            "🔗 O copia el enlace manualmente:\n"
            "`https://1wtsks.com/v3/landing-fortune-wheel?p=gv72`\n"
            "_(si no se abre, simplemente pégalo en cualquier navegador)_\n\n"
            "4️⃣ Al registrarte, introduce el código promocional:\n"
            "🎁 `MOB500RR`\n"
            "Activará la conexión con el bot y te dará bonos 💰\n\n"
            "⚠️ **Sin completar todos los pasos, el bot no podrá conectarse a tu cuenta**\n"
            "Así que no te saltes ningún punto 🛠"
        ),
        'register_button_text': "Ir al registro 🔗",
        'steps_done_button': "Todos los pasos completados 🛠",
        'instruction_2': (
            "🎉 ¡Genial! Ya estamos en la recta final\n"
            "¡Falta muy poco para que puedas comprobar por ti mismo que el bot funciona como un reloj! ⏱️🤖\n\n"
            "📌 **Ahora necesito saber tu ID** —\n"
            "es necesario para que el bot sepa qué sesiones debe verificar. Sin esto, no podrá conectarse a ti correctamente 🙈\n\n"
            "🧭 **Cómo encontrar tu ID:**\n"
            "Simplemente haz clic en el botón de tu perfil (como se muestra en las instrucciones) y envíamelo.\n"
            "Puedes:\n"
            "✅ Escribir el ID como texto — es la forma más rápida\n"
            "📸 O enviar una captura de pantalla con el ID — ¡también funciona!\n\n"
            "¡Te espero! 💌"
        ),
        'send_id_button': "Enviar mi ID y conectarlo al bot🛠",
        'prompt_for_id': "Envía tu ID o una foto directamente a este chat 👇",
        'id_received': (
            "¡Recibido! 👍\n\n"
            "Todas las operaciones se realizan manualmente, ya que el sistema es complejo y no se puede automatizar. Nuestro equipo ya ha recibido todos tus datos y está trabajando para añadirte a las listas de acceso. Y, como prometí, todo es completamente gratis.\n\n"
            "Puedo permitirme pagar la cantidad requerida por ti, y en el futuro, tú también podrás usar el dinero para ayudar a otros 😉\n\n"
            "¡Te escribiré tan pronto como todo esté listo!"
        ),
        'wrong_data_button': "Envié los datos incorrectos ⚠️",
        'change_data_prompt': "Cambiaré los datos de la cuenta si se enviaron por error. Por favor, envía los datos correctos.",
        'data_changed': "Tus datos han sido cambiados y he notificado al personal sobre los cambios✍️",
        'support_button': "Contactar con soporte 👨‍💻",
        'access_granted': (
            "🎉 **¡Felicidades! ¡Acceso concedido!**\n"
            "Has sido conectado exitosamente a la aplicación que ayuda a conocer los resultados de cualquiera de tus juegos en Mines 💣 — ¡ahora todo está bajo control! 🧠💸\n\n"
            "📌 **Algunas reglas para que todo funcione perfectamente:**\n"
            "Nuestro bot solo analiza juegos reales que ocurren en el sistema oficial.\n"
            "❗️**El bot no funciona en modo de demostración.**\n\n"
            "🔧 **Cómo usar el bot:**\n\n"
            "1️⃣ Inicia el juego, haz una apuesta, ¡pero no presiones nada!\n"
            "2️⃣ Ve a la mini-aplicación del bot y presiona el botón 'Analisar padrão' 🔍\n"
            "3️⃣ Recibe la lista de casillas seguras ✅\n"
            "4️⃣ ¡Repite los movimientos que sugiere el bot y retira el dinero! 💰🎯\n\n"
            "⚠️ **Importante:**\n"
            "No te arriesgues por intuición. Gana dinero con la cabeza fría y solo en las casillas verificadas 🧊🧠"
        ),
        'open_app_button': "Abrir aplicación 📲",
        'access_denied': "Lo sentimos, pero después de la verificación, se encontraron razones por las que no podemos darte acceso al bot.",
        'access_temp_denied': (
            "🚫 **¡Vaya! Acceso no concedido**\n"
            "Lamentablemente, la conexión con el bot falló 😔\n\n"
            "📌 Por favor, sigue atentamente las recomendaciones de nuestro empleado para que todo salga bien.\n"
            "Esto es lo que dice:\n"
            "📝 _«{comment}»_"
        ),
    }
}


# --- ИНИЦИАЛИЗАЦИЯ БОТА И БД / INICIALIZAÇÃO DO BOT E DO BD ---

bot = telebot.TeleBot(BOT_TOKEN)

# Функция для загрузки данных пользователей из файла
# Função para carregar os dados dos usuários a partir de um arquivo
def load_db():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, 'r', encoding='utf-8') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {} # Возвращаем пустой словарь, если файл пуст или поврежден
    return {}

# Функция для сохранения данных пользователей в файл
# Função para salvar os dados dos usuários em um arquivo
def save_db(db):
    with open(DB_FILE, 'w', encoding='utf-8') as f:
        json.dump(db, f, indent=4, ensure_ascii=False)

# Загружаем базу данных при старте
# Carregamos o banco de dados na inicialização
db = load_db()

# Функция для получения текста на нужном языке
# Função para obter o texto no idioma correto
def get_text(key, lang='ru', **kwargs):
    # Если язык не найден, используется русский по умолчанию
    # Se o idioma não for encontrado, o russo é usado como padrão
    text = TEXTS.get(lang, TEXTS['ru']).get(key, f"_{key}_")
    return text.format(**kwargs)

# Функция для получения данных пользователя
# Função para obter os dados de um usuário
def get_user_data(user_id):
    user_id_str = str(user_id)
    if user_id_str not in db:
        db[user_id_str] = {
            'lang': None,
            'state': 'start', # 'start', 'awaiting_id', 'pending_review', 'approved', 'rejected'
            '1win_id': None,
            'status': 'user' # 'user' or 'admin'
        }
    return db[user_id_str]

# --- КЛАВИАТУРЫ / TECLADOS ---

# Клавиатура выбора языка
# Teclado de seleção de idioma
def language_keyboard():
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn_pt = types.InlineKeyboardButton("Português 🇧🇷", callback_data='lang_pt')
    btn_es = types.InlineKeyboardButton("Español 🇪🇸", callback_data='lang_es')
    btn_ru = types.InlineKeyboardButton("Русский 🇷🇺", callback_data='lang_ru')
    markup.add(btn_pt, btn_es, btn_ru)
    return markup

# Универсальная клавиатура с кнопкой поддержки
# Teclado universal com botão de suporte
def support_keyboard(lang):
    markup = types.InlineKeyboardMarkup()
    support_btn = types.InlineKeyboardButton(text=get_text('support_button', lang), url=SUPPORT_LINK)
    markup.add(support_btn)
    return markup

# --- ОБРАБОТЧИКИ ДЛЯ ИГРОКОВ / HANDLERS PARA JOGADORES ---

# Обработчик команды /start
# Handler para o comando /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    user_id = message.chat.id
    
    # Проверяем, является ли пользователь админом
    # Verificamos se o usuário é um administrador
    if user_id in ADMIN_IDS:
        handle_admin_panel(message)
        return

    # Для обычных пользователей
    # Para usuários comuns
    user_data = get_user_data(user_id)
    
    # Если язык еще не выбран, показываем выбор
    # Se o idioma ainda não foi escolhido, mostramos a seleção
    if not user_data.get('lang'):
        bot.send_message(user_id, get_text('choose_lang'), reply_markup=language_keyboard())
    else:
        # Если пользователь уже в системе, отправляем его на нужный шаг
        # Se o usuário já está no sistema, o enviamos para a etapa correta
        route_user(message)

# Функция-маршрутизатор для пользователя
# Função de roteamento para o usuário
def route_user(message):
    user_id = message.chat.id
    user_data = get_user_data(user_id)
    lang = user_data.get('lang', 'ru')
    state = user_data.get('state', 'start')

    if state == 'start':
        markup = types.InlineKeyboardMarkup()
        btn_sync = types.InlineKeyboardButton(text=get_text('sync_button', lang), callback_data='sync_account')
        support_btn = types.InlineKeyboardButton(text=get_text('support_button', lang), url=SUPPORT_LINK)
        markup.add(btn_sync)
        markup.add(support_btn)
        bot.send_message(user_id, get_text('welcome', lang), reply_markup=markup, parse_mode='Markdown')
    
    elif state == 'awaiting_id':
        markup = types.InlineKeyboardMarkup()
        btn_send_id = types.InlineKeyboardButton(text=get_text('send_id_button', lang), callback_data='prompt_for_id')
        support_btn = types.InlineKeyboardButton(text=get_text('support_button', lang), url=SUPPORT_LINK)
        markup.add(btn_send_id)
        markup.add(support_btn)
        bot.send_message(user_id, get_text('instruction_2', lang), reply_markup=markup, parse_mode='Markdown')

    elif state == 'pending_review':
        markup = types.InlineKeyboardMarkup()
        btn_wrong_data = types.InlineKeyboardButton(text=get_text('wrong_data_button', lang), callback_data='change_data')
        support_btn = types.InlineKeyboardButton(text=get_text('support_button', lang), url=SUPPORT_LINK)
        markup.add(btn_wrong_data)
        markup.add(support_btn)
        bot.send_message(user_id, get_text('id_received', lang), reply_markup=markup, parse_mode='Markdown')

    elif state == 'approved':
        markup = types.InlineKeyboardMarkup()
        # Создаем кнопку-ссылку на Web App
        # Criamos um botão de link para o Web App
        web_app = types.WebAppInfo(MINI_APP_URL)
        btn_open_app = types.InlineKeyboardButton(text=get_text('open_app_button', lang), web_app=web_app)
        support_btn = types.InlineKeyboardButton(text=get_text('support_button', lang), url=SUPPORT_LINK)
        markup.add(btn_open_app)
        markup.add(support_btn)
        bot.send_message(user_id, get_text('access_granted', lang), reply_markup=markup, parse_mode='Markdown')

    elif state == 'rejected':
        bot.send_message(user_id, get_text('access_denied', lang), reply_markup=support_keyboard(lang), parse_mode='Markdown')

# Обработчик нажатий на инлайн-кнопки
# Handler para cliques em botões inline
@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    user_id = call.message.chat.id
    user_data = get_user_data(user_id)
    lang = user_data.get('lang', 'ru')
    
    # --- Админские колбэки ---
    # --- Callbacks de administrador ---
    if user_id in ADMIN_IDS:
        handle_admin_callback(call)
        return

    # --- Пользовательские колбэки ---
    # --- Callbacks de usuário ---
    if call.data.startswith('lang_'):
        lang_code = call.data.split('_')[1]
        user_data['lang'] = lang_code
        save_db(db)
        bot.delete_message(user_id, call.message.message_id)
        route_user(call.message) # Перенаправляем на первый шаг
        return

    if call.data == 'sync_account':
        # ИЗМЕНЕНО: Добавлена кнопка для регистрации
        # ALTERADO: Adicionado botão para registro
        markup = types.InlineKeyboardMarkup(row_width=1)
        registration_url = "https://1wtsks.com/v3/landing-fortune-wheel?p=gv72"
        
        btn_register = types.InlineKeyboardButton(text=get_text('register_button_text', lang), url=registration_url)
        btn_steps_done = types.InlineKeyboardButton(text=get_text('steps_done_button', lang), callback_data='steps_done')
        support_btn = types.InlineKeyboardButton(text=get_text('support_button', lang), url=SUPPORT_LINK)
        
        markup.add(btn_register, btn_steps_done, support_btn)
        
        bot.edit_message_text(chat_id=user_id, message_id=call.message.message_id, text=get_text('instruction_1', lang), reply_markup=markup, parse_mode='Markdown')

    elif call.data == 'steps_done':
        user_data['state'] = 'awaiting_id'
        save_db(db)
        markup = types.InlineKeyboardMarkup()
        btn_send_id = types.InlineKeyboardButton(text=get_text('send_id_button', lang), callback_data='prompt_for_id')
        support_btn = types.InlineKeyboardButton(text=get_text('support_button', lang), url=SUPPORT_LINK)
        markup.add(btn_send_id)
        markup.add(support_btn)
        bot.edit_message_text(chat_id=user_id, message_id=call.message.message_id, text=get_text('instruction_2', lang), reply_markup=markup, parse_mode='Markdown')

    elif call.data == 'prompt_for_id':
        bot.send_message(user_id, get_text('prompt_for_id', lang))
        bot.answer_callback_query(call.id) # Убираем "часики" с кнопки

    elif call.data == 'change_data':
        user_data['state'] = 'awaiting_id' # Возвращаем на шаг ожидания ID
        save_db(db)
        bot.send_message(user_id, get_text('change_data_prompt', lang))
        bot.answer_callback_query(call.id)


# Обработчик получения ID от пользователя (текст или фото)
# Handler para receber o ID do usuário (texto ou foto)
@bot.message_handler(content_types=['text', 'photo'])
def handle_id_submission(message):
    user_id = message.chat.id
    
    if user_id in ADMIN_IDS:
        handle_admin_messages(message)
        return
        
    user_data = get_user_data(user_id)
    lang = user_data.get('lang', 'ru')
    
    if user_data['state'] == 'awaiting_id':
        # Сохраняем ID. Если фото, сохраняем file_id для пересылки админу
        # Salvamos o ID. Se for uma foto, salvamos o file_id para encaminhar ao administrador
        if message.text:
            # Игнорируем команды, которые могут быть введены случайно
            if message.text.startswith('/'):
                return
            user_data['1win_id'] = message.text
        elif message.photo:
            user_data['1win_id'] = message.photo[-1].file_id

        # Меняем статус и сохраняем
        # Mudamos o status e salvamos
        user_data['state'] = 'pending_review'
        
        # Добавляем в очередь на проверку
        # Adicionamos à fila de verificação
        if 'pending_requests' not in db:
            db['pending_requests'] = []
        if str(user_id) not in db['pending_requests']:
             db['pending_requests'].append(str(user_id))

        save_db(db)

        # Отправляем подтверждение
        # Enviamos a confirmação
        markup = types.InlineKeyboardMarkup()
        btn_wrong_data = types.InlineKeyboardButton(text=get_text('wrong_data_button', lang), callback_data='change_data')
        support_btn = types.InlineKeyboardButton(text=get_text('support_button', lang), url=SUPPORT_LINK)
        markup.add(btn_wrong_data)
        markup.add(support_btn)
        
        # Если данные были изменены, отправляем другое сообщение
        # Se os dados foram alterados, enviamos outra mensagem
        if hasattr(message, 'reply_to_message') and message.reply_to_message and "изменю данные" in message.reply_to_message.text.lower():
             bot.send_message(user_id, get_text('data_changed', lang))
        else:
             bot.send_message(user_id, get_text('id_received', lang), reply_markup=markup)


# --- ОБРАБОТЧИКИ ДЛЯ АДМИНОВ / HANDLERS PARA ADMINISTRADORES ---

# Панель администратора
# Painel do administrador
def handle_admin_panel(message):
    user_id = message.chat.id
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton(get_text('incoming_requests_button'))
    btn2 = types.KeyboardButton(get_text('stats_button'))
    btn3 = types.KeyboardButton(get_text('status_button'))
    markup.add(btn1, btn2, btn3)
    bot.send_message(user_id, get_text('admin_panel_title'), reply_markup=markup)

# Обработка текстовых сообщений от админа
# Processamento de mensagens de texto do administrador
def handle_admin_messages(message):
    user_id = message.chat.id
    user_data = get_user_data(user_id)
    
    # Если админ отправляет комментарий для отказа
    # Se o administrador está enviando um comentário para rejeição
    if user_data.get('state') == 'awaiting_rejection_comment':
        target_user_id = user_data.get('target_user_id')
        comment = message.text
        
        # Отправляем сообщение пользователю
        # Enviamos a mensagem ao usuário
        target_user_data = get_user_data(target_user_id)
        target_lang = target_user_data.get('lang', 'ru')
        bot.send_message(target_user_id, get_text('access_temp_denied', target_lang, comment=comment), reply_markup=support_keyboard(target_lang), parse_mode='Markdown')
        
        # Обновляем статус пользователя
        # Atualizamos o status do usuário
        target_user_data['state'] = 'rejected'
        if 'pending_requests' in db and str(target_user_id) in db['pending_requests']:
            db['pending_requests'].remove(str(target_user_id))
        
        # Возвращаем админа в нормальное состояние
        # Retornamos o administrador ao estado normal
        user_data['state'] = 'admin'
        user_data['target_user_id'] = None
        save_db(db)
        
        bot.send_message(user_id, get_text('request_rejected_with_comment', user_id=target_user_id))
        # Показываем следующую заявку, если есть
        # Mostramos a próxima solicitação, se houver
        show_next_request(user_id)
        return

    # Обработка кнопок из ReplyKeyboard
    # Processamento de botões do ReplyKeyboard
    if message.text == get_text('incoming_requests_button'):
        show_next_request(user_id)
    elif message.text == get_text('stats_button'):
        show_stats(user_id)
    elif message.text == get_text('status_button'):
        bot.send_message(user_id, get_text('bot_status_ok'))

# Показать следующую заявку на проверку
# Mostrar a próxima solicitação para verificação
def show_next_request(admin_id):
    pending = db.get('pending_requests', [])
    if not pending:
        bot.send_message(admin_id, get_text('no_pending_requests'))
        return
    
    target_user_id_str = pending[0]
    target_user_data = get_user_data(target_user_id_str)
    user_1win_id = target_user_data.get('1win_id', 'N/A')
    
    # Создаем клавиатуру для действий
    # Criamos o teclado para as ações
    markup = types.InlineKeyboardMarkup()
    btn_accept = types.InlineKeyboardButton(get_text('accept_button'), callback_data=f"admin_accept_{target_user_id_str}")
    btn_reject = types.InlineKeyboardButton(get_text('reject_button'), callback_data=f"admin_reject_{target_user_id_str}")
    btn_reject_comment = types.InlineKeyboardButton(get_text('reject_with_comment_button'), callback_data=f"admin_comment_{target_user_id_str}")
    markup.add(btn_accept, btn_reject)
    markup.add(btn_reject_comment)
    
    # Если ID - это file_id фотографии, отправляем фото, иначе текст
    # Se o ID for um file_id de uma foto, enviamos a foto, caso contrário, o texto
    try:
        # Пытаемся отправить как фото
        # Tentamos enviar como foto
        bot.send_photo(admin_id, user_1win_id, caption=get_text('request_from_user', user_id=target_user_id_str, user_data=f"Фото ID"), reply_markup=markup)
    except telebot.apihelper.ApiTelegramException:
        # Если не фото, отправляем как текст
        # Se não for uma foto, enviamos como texto
        bot.send_message(admin_id, get_text('request_from_user', user_id=target_user_id_str, user_data=user_1win_id), reply_markup=markup)

# Показать статистику
# Mostrar estatísticas
def show_stats(admin_id):
    accepted_count = 0
    rejected_count = 0
    for user_id, data in db.items():
        if user_id.isdigit(): # Исключаем служебные записи
            if data.get('state') == 'approved':
                accepted_count += 1
            elif data.get('state') == 'rejected':
                rejected_count += 1
    
    pending_count = len(db.get('pending_requests', []))
    
    bot.send_message(admin_id, get_text('stats_info', accepted=accepted_count, rejected=rejected_count, pending=pending_count), parse_mode='Markdown')

# Обработка колбэков от админа
# Processamento de callbacks do administrador
def handle_admin_callback(call):
    admin_id = call.message.chat.id
    try:
        action, target_user_id_str = call.data.split('_', 2)[1:]
    except ValueError:
        bot.answer_callback_query(call.id, "Ошибка: неверный формат callback_data")
        return
        
    target_user_id = int(target_user_id_str)
    
    target_user_data = get_user_data(target_user_id)
    target_lang = target_user_data.get('lang', 'ru')
    
    # Убираем заявку из очереди
    # Removemos a solicitação da fila
    if 'pending_requests' in db and target_user_id_str in db['pending_requests']:
        db['pending_requests'].remove(target_user_id_str)
    
    if action == 'accept':
        target_user_data['state'] = 'approved'
        save_db(db)
        
        # Отправляем сообщение пользователю
        # Enviamos a mensagem ao usuário
        markup = types.InlineKeyboardMarkup()
        web_app = types.WebAppInfo(MINI_APP_URL)
        btn_open_app = types.InlineKeyboardButton(text=get_text('open_app_button', target_lang), web_app=web_app)
        support_btn = types.InlineKeyboardButton(text=get_text('support_button', target_lang), url=SUPPORT_LINK)
        markup.add(btn_open_app)
        markup.add(support_btn)
        bot.send_message(target_user_id, get_text('access_granted', target_lang), reply_markup=markup, parse_mode='Markdown')
        
        bot.edit_message_text(chat_id=admin_id, message_id=call.message.message_id, text=get_text('request_accepted', user_id=target_user_id))
        show_next_request(admin_id) # Показываем следующую заявку
        
    elif action == 'reject':
        target_user_data['state'] = 'rejected'
        save_db(db)
        bot.send_message(target_user_id, get_text('access_denied', target_lang), reply_markup=support_keyboard(target_lang))
        bot.edit_message_text(chat_id=admin_id, message_id=call.message.message_id, text=get_text('request_rejected', user_id=target_user_id))
        show_next_request(admin_id)
        
    elif action == 'comment':
        admin_data = get_user_data(admin_id)
        admin_data['state'] = 'awaiting_rejection_comment'
        admin_data['target_user_id'] = target_user_id
        save_db(db)
        
        bot.edit_message_text(chat_id=admin_id, message_id=call.message.message_id, text=get_text('prompt_for_rejection_comment', user_id=target_user_id))
        
    bot.answer_callback_query(call.id)


# --- ЗАПУСК БОТА / INICIAR O BOT ---
if __name__ == '__main__':
    print("Бот запускается... / O bot está iniciando...")
    # Проверяем токен
    # Verificamos o token
    if BOT_TOKEN == 'YOUR_BOT_TOKEN_HERE':
        print("\n!!! ВНИМАНИЕ !!!")
        print("Пожалуйста, вставьте ваш токен в переменную BOT_TOKEN на строке 10.")
        print("\n!!! ATENÇÃO !!!")
        print("Por favor, insira o seu token na variável BOT_TOKEN na linha 10.")
    else:
        print("Бот запущен. / Bot iniciado.")
        bot.polling(none_stop=True)








