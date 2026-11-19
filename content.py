# -*- coding: utf-8 -*-
"""
Contenido de la Máquina de Convencimiento (Pulso bot de Omnicracia).
Todo el texto vive aquí para que lo edites sin tocar la lógica.

Candados: CERO MENTIRAS · pacífico, legal, apartidista · sin líder · cero rojo.
Remate oficial: "Ellos necesitan de nosotros, no nosotros de ellos."  ·  Grito: "SOY OMNICRACIA."
Motor de cada mensaje: MASA (siente la ola) -> VALOR (algo del códice que empodera) -> CONFIRMO (un toque que reafirma identidad).
"""

# ------------------------------------------------------------------ ENLACES
LINKS = {
    "canal": "https://whatsapp.com/channel/0029Vb9URZW7IUYdUMhH4L1B",
    "telegram_canal": "https://t.me/omnicracia",
    "zoom": "https://us06web.zoom.us/j/89866033549?pwd=ADZEluMjVgzZtH984UeNsavKqWXeVd.1",
    "web": "https://omnicracia.com",
    "revocacion": "https://omnicracia.com/revocacion",
    "omnia_bot": "https://t.me/Omnicracia_Omnia_bot",   # el clon Delphi (preguntas abiertas)
}

REMATE = "Ellos necesitan de nosotros, no nosotros de ellos."
GRITO = "SOY OMNICRACIA."

# ------------------------------------------------------------------ ONBOARDING (3 toques)
# Toque 1 = al dar /start. Toque 2 = al primer CONFIRMO. Toque 3 = segundo día.
ONBOARDING = {
    "t1_welcome": (
        "No estás solo. 💜 Ya somos casi *MEDIO MILLÓN* de mexicanos en los 32 estados, y cada día nos sumamos más.\n\n"
        "Bienvenid@ a Omnicracia: la mayoría —pacífica, legal y sin partido— tomando el control. "
        "Aquí nadie busca el poder: *el poder es tuyo.*\n"
        "Acabas de hacer lo que millones no se atreven. Ya eres imparable.\n\n"
        "Esto es simple: cada día te llega el *Pulso* — 30 segundos que te mantienen fuerte, informado y en sintonía con todos. "
        "El que se informa, no se apaga.\n\n"
        "Toca el botón de abajo y arranca tu racha. 💜"
    ),
    "t2_after_first_confirm": (
        "🔥 *¡Racha iniciada! Día 1.*\n"
        "Acabas de hacer algo que el 99% no hace: comprometerte y cumplir el mismo día.\n\n"
        "Te voy a ser honesto: México no se arregla por un héroe de un día. Se arregla porque millones aparecemos *todos los días*. "
        "La constancia es nuestra arma secreta — y la tuya empieza hoy.\n\n"
        "Mañana te mando el Pulso. Un toque, 30 segundos, y no rompes la racha. ¿Trato hecho? 💜"
    ),
    "t3_first_mission": (
        "Día 2, y aquí sigues. 💪 Así se ve un omnícrata de verdad: constante.\n\n"
        "Tu primera misión, la más poderosa y la más fácil: piensa en *UNA* persona que también está harta y mándale esto 👇\n\n"
        "_\"Me uní a Omnicracia: casi medio millón sin partido, pacífico y legal, para que el país funcione. Entra: omnicracia.com\"_\n\n"
        "Con eso ya multiplicaste. Cuando lo hagas, escribe *HECHO* y te subo de nivel. 🔥"
    ),
}

# ------------------------------------------------------------------ PULSO DIARIO (ciclo perpetuo de 30)
# Cada día: (titulo, cuerpo, texto_del_boton_confirmo)
# El cuerpo ya trae MASA + VALOR; el CONFIRMO es el botón.
PULSO = [
    ("Bienvenida",
     "No estás solo. 💜 Ya somos casi *MEDIO MILLÓN* de mexicanos hartos de lo mismo, en los 32 estados — y hoy se sumaron más. "
     "Esto no es un grupo de quejas: es la mayoría despertando. Y tú eres parte.",
     "💜 Hoy confirmo"),

    ("Qué es",
     "Omnicracia en una frase: *el poder de todos, en manos de todos.* No es partido. Nadie busca la silla. El dueño del país eres tú. "
     "Entiéndelo una vez y nadie te vuelve a confundir jamás.",
     "✅ Lo tengo claro"),

    ("Quién eres ahora",
     "¿Por qué \"omnícrata\"? Porque dejaste de ser espectador. Ya no te quejas en silencio: te organizas. Eso te cambia de bando. "
     "Entre los que miran y los que mueven, hoy *tú mueves*.",
     "🔥 Hoy mando yo"),

    ("Sin líder",
     "Aquí no hay caudillo que te salve — y esa es nuestra fuerza más grande. A un jefe lo compran, lo callan o lo traicionan. "
     "A millones organizados, *no hay cómo*. No esperamos salvador: el salvador somos todos.",
     "👍 Así no nos paran"),

    ("La ventaja",
     "Dato que te va a gustar: una minoría organizada *SIEMPRE* le gana a una mayoría dispersa. Lo único que nos faltaba era juntarnos. "
     "Y mira dónde vamos: casi medio millón, y cada día más.",
     "💜 Sigo dentro"),

    ("El grito",
     "Dilo fuerte: *SOY OMNICRACIA.* No es un hashtag. Es decidir que tu país te importa más que tu miedo. "
     "Los que lo dicen y lo sostienen son los que cambian la historia.",
     "📣 SOY OMNICRACIA"),

    ("La pregunta que despierta",
     "Hoy, una sola cosa: pregúntale a alguien que amas: *\"¿confías en que si te pasa algo, en México habrá justicia?\"* "
     "Su respuesta es por lo que estamos aquí. Y si se queda pensando… ya plantaste la semilla.",
     "🙋 Voy a preguntar"),

    ("El voto",
     "Votar cada 6 años no es poder: es pedir permiso y callarte un sexenio. ¿A eso le llaman democracia? "
     "Nosotros queremos mandar *todos los días*, no uno cada seis años.",
     "✊ Quiero mandar diario"),

    ("Mismo robo",
     "Cambian las siglas. Nunca tu vida. Mismo robo, otro logo. No falló un partido: *falló el sistema completo*. "
     "Por eso no peleamos contra un color — peleamos contra lo que no sirve, gane quien gane.",
     "👍 De acuerdo"),

    ("La justicia",
     "9 de cada 10 delitos quedan impunes. Pagas impuestos por una justicia que nunca te llega. "
     "¿Y a quién le reclamas? A los mismos que viven de que no haya.",
     "💜 Ya no lo acepto"),

    ("La trampa",
     "Te hacen creer que tienes que escoger entre malos. *Esa es la trampa.* La salida no es otro partido: "
     "es otro sistema, uno donde el que la hace, la paga.",
     "👁 Ya la vi"),

    ("El empleado",
     "No te representan: te cuestan. Y no le rinden cuentas a nadie. En cualquier chamba, al que no da resultados se le corre. "
     "*¿Por qué con ellos no?*",
     "🔥 Yo los correría"),

    ("La rabia",
     "¿Te enoja? Bien. Esa rabia es gasolina. Sola no sirve; *organizada, es imparable*. "
     "Guárdala — y hoy confírmame que sigues firme.",
     "🔥 Aquí sigo firme"),

    ("Mira alrededor",
     "El hospital sin medicina, el agua que no llega, el sueldo que no alcanza. No es mala suerte: *es un sistema diseñado así*. "
     "Y se rediseña juntos.",
     "💜 Lo veo claro"),

    ("La obediencia",
     "Escúchalo bien: ningún poder existe si la gente deja de obedecer. *Ninguno.* "
     "El día que la mayoría dice \"ya no\", se acabó. Ese poder siempre fue tuyo.",
     "💜 Lo entendí"),

    ("El remate",
     "Ellos te necesitan a ti. Tú no los necesitas a ellos. De tu trabajo, de tus impuestos, de tu silencio: de ahí viven.\n\n"
     "*" + REMATE + "*",
     "💪 De ellos no"),

    ("El 99%",
     "No hay empresa sin clientes. No hay gobierno sin ciudadanos. *Somos el 99%.* "
     "Lo único que faltaba era unirnos. Ya empezamos — casi medio millón.",
     "✊ Soy del 99%"),

    ("El blindaje",
     "¿Por qué no nos pueden parar? Porque el plan no está en una cabeza: *está en todas. En la tuya también.* "
     "Quitan a uno, siguen millones.",
     "💜 Me sé el para qué"),

    ("La cuenta",
     "La cuenta que les quita el sueño: tú traes a 3, esos 3 traen a 3… en pocos pasos somos millones. "
     "*Las matemáticas son nuestras.*",
     "➕ Le entro al 3x3"),

    ("A quién sumar",
     "No tienes que convencer a todo México. Solo suma a los que *YA* están hartos. Tú, multiplicado. Eso es fuerza de verdad.",
     "🔥 Ya sé a quién"),

    ("De boca en boca",
     "Tarea de hoy: dile a UNA persona harta \"únete, ya somos casi medio millón\" y pásale omnicracia.com. "
     "*Así crece esto: de boca en boca.*",
     "🙋 Lo mando hoy"),

    ("El arma",
     "Nuestra arma no es la violencia: es dejar de obedecer lo que nos daña. No comprar, no participar, no callar. "
     "*Pacífico. Legal. Y por eso, imparable.*",
     "👍 Pacífico y legal"),

    ("La cita",
     "📅 La cita sagrada: cada *MIÉRCOLES 9 PM* (CDMX), junta nacional por Zoom. Ahí nos sincronizamos y decidimos juntos. "
     "Pon la alarma — ahí se cocina todo.",
     "📅 Ahí estaré"),

    ("La disciplina",
     "El secreto que nadie te dice: no gana el más valiente, *gana el más constante*. "
     "México no cambia por un día heroico; cambia porque millones aparecemos TODOS los días. Tu racha es tu fuerza.",
     "💜 No rompo la racha"),

    ("Tu talento",
     "¿Tienes un talento? Memes, cámara, edición, diseño, voz. *El movimiento te necesita; aquí nadie sobra.* "
     "Escribe APORTAR y te sumamos al Escuadrón. 🔥",
     "🙌 Quiero aportar"),

    ("Infórmate",
     "El que informa, gana. Antes de compartir, entiende. Léete el *Canon del Omnícrata* una vez y nunca más te van a poder confundir. "
     "Escribe CANON y te lo mando.",
     "📖 Me sé el Canon"),

    ("Las 6 leyes",
     "Las 6 leyes que nunca se rompen: *mayoría, pacíficos, legales, sin partido, sin líder, con la verdad.* "
     "Si alguien te pide romper una, no es de los nuestros.",
     "💜 Las hago mías"),

    ("Trae a 3",
     "Haz una cosa por México: *trae a 3* que de verdad estén hartos. No a todos. A 3. Esos 3 harán lo mismo. Así ganamos.",
     "🙋 Traigo a 3"),

    ("Unidos",
     "Nos quieren divididos, asustados y solos. Nuestra respuesta: *unidos, organizados y en paz.* "
     "Ya somos casi medio millón, y tú llegaste para quedarte.",
     "💜 Sigo firme"),

    ("El cierre",
     "Ya lo sabes todo. Ya no eres espectador: *eres omnícrata.* Ahora ve y haz que otro lo sea.\n\n"
     "*" + REMATE + "  " + GRITO + "* 💜\n"
     "(Mañana arrancamos de nuevo — porque los constantes ganan.)",
     "📣 SOY OMNICRACIA"),
]

# ------------------------------------------------------------------ RACHA (reconfirmación)
def racha_message(racha: int) -> str:
    """Mensaje que acompaña cada CONFIRMO diario. Reafirma identidad + hitos."""
    base = f"¡Confirmado! 💜 Llevas *{racha}* día(s) firme. Eres de los constantes — de los que de verdad cambian el país."
    hito = ""
    if racha == 3:
        hito = "\n\n✨ 3 días seguidos. Ya tomó forma el hábito. No pares."
    elif racha == 7:
        # Primera invitación al Canal (de Telegram): ya hay compromiso probado (una semana firme).
        hito = ("\n\n🏅 ¡Una semana sin fallar! Ya eres columna del movimiento.\n"
                "Ya estás list@ para el siguiente paso: entra al *Canal de Omnicracia en Telegram* "
                "y siente la ola completa, ahora sí con determinación 👉 " + LINKS["telegram_canal"])
    elif racha == 14:
        hito = "\n\n⚡ 14 días. Eres de los que no se apagan. Imparable."
    elif racha == 30:
        hito = ("\n\n👑 30 días. Eres imparable. Ahora ayuda a otro a empezar su racha.\n"
                "Y si aún no estás en el *Canal de Omnicracia en Telegram*, este es tu momento 👉 " + LINKS["telegram_canal"])
    elif racha > 30 and racha % 30 == 0:
        hito = f"\n\n👑 {racha} días. Leyenda viva del movimiento."
    cierre = "\n\nNos vemos mañana. No la rompas. 🔥"
    return base + hito + cierre

# ------------------------------------------------------------------ MENSAJES DE SISTEMA
SYS = {
    "already_confirmed": "Ya confirmaste hoy. 💜 Tu racha va en *{racha}*. Nos vemos mañana — no la rompas. 🔥",
    "paused": "Listo, pausé tu Pulso. 💜 Cuando quieras volver, escribe *REANUDAR*. El movimiento no para, y tu lugar aquí sigue.",
    "resumed": "¡Qué bueno que volviste! 💜 Retomamos el Pulso hoy mismo. Los que vuelven son los que de verdad quieren. 🔥",
    "mission_done": "🔥 ¡ESO! Acabas de multiplicar. Un omnícrata más por ti. Así, de uno en uno, nos volvemos imparables. "
                    "Sigue trayendo gente harta — cada \"trae a 3\" nos acerca a cambiarlo todo. 💜",
    "fallback": (
        "Te leo. 💜 Para que no se te pase nada:\n"
        "• Escribe *CANON* y te paso el Canon del Omnícrata.\n"
        "• Escribe *JUNTA* para la junta de los miércoles.\n"
        "• Escribe *APORTAR* si quieres sumar tu talento.\n\n"
        "¿Tienes una duda más de fondo? Pregúntale a *Omnia*, que te contesta lo que sea 👇"
    ),
    "help": (
        "Soy tu Pulso diario de Omnicracia. 💜 Cada día te mando 30 segundos que te mantienen fuerte y en sintonía.\n\n"
        "Comandos:\n"
        "• *CONFIRMO* o el botón — marca tu día y sube tu racha.\n"
        "• *CANON* — el Canon del Omnícrata.\n"
        "• *JUNTA* — la junta de los miércoles.\n"
        "• *APORTAR* — suma tu talento.\n"
        "• *PAUSA* / *REANUDAR* — pausar o volver.\n\n"
        + REMATE + "  " + GRITO
    ),
}

# ------------------------------------------------------------------ CANON de bolsillo (respuesta a CANON)
CANON_POCKET = (
    "📖 *CANON DEL OMNÍCRATA* (versión de bolsillo)\n\n"
    "• *Qué es:* el poder de todo, en el poder de todos. No es partido, nadie busca la silla: la mayoría vigila, decide y sanciona.\n"
    "• *Las 6 leyes:* mayoría, pacíficos, legales, sin partido, sin líder, con la verdad.\n"
    "• *El poder:* ellos viven de nosotros; el día que dejamos de obedecer, se acabó.\n"
    "• *Cómo crecemos:* trae a 3, que traen a 3.\n"
    "• *La cita:* junta nacional, miércoles 9 PM (CDMX).\n"
    "• *El blindaje:* todos sabemos lo mismo; quitar a uno no detiene a nadie.\n\n"
    "*" + REMATE + "  " + GRITO + "* 💜\n\n"
    "Léelo completo aquí 👉 " + LINKS["web"]
)

# ------------------------------------------------------------------ FAQ (preguntas REALES del clon, voz de judo + cierre con paso)
# Cada item: (lista de palabras clave en minúsculas sin acento, respuesta)
# Se busca por "contiene". Van de lo más específico a lo general.
FAQ = [
    (["lider", "quien manda", "jefe", "cabeza", "consejo"],
     "Te voy a decir algo que te va a volar la cabeza: Omnicracia *NO tiene un líder* — y esa es su fuerza más grande. 💜\n\n"
     "A cada movimiento con un solo jefe lo compran, lo amenazan o se le sube el poder y traiciona. Aquí no hay a quién comprar… porque mandamos todos. "
     "Lo grande se decide juntos, en la junta nacional de cada miércoles.\n\n"
     "No esperamos un salvador. El salvador somos nosotros, millones, organizados. ¿Le entras? Confirma tu día con el botón del Pulso. 🔥"),

    (["ilegal", "anticonstitucional", "constitucion", "derrocar", "golpe", "violencia", "violento"],
     "Gran pregunta, y la respuesta te va a dar tranquilidad: Omnicracia es *100% legal, pacífica y constitucional*. "
     "No queremos derrocar nada por la fuerza. Al revés: usamos las herramientas que la propia ley nos da, como la revocación de mandato, que es un *derecho* en la Constitución.\n\n"
     "Y no es menos democracia: es *más*. Que la gente no solo vote cada 6 años, sino que vigile, decida y exija todos los días. "
     "El único \"choque\" es con los que viven cómodos de que tú no participes. 🛡️"),

    (["partido", "morena", "pri", "pan", "mc", "oposicion", "candidato", "por quien voto", "izquierda", "derecha"],
     "Omnicracia *NO es un partido* ni apoya a ninguno, y jamás te vamos a decir por quién votar. 💜\n\n"
     "El enemigo no es un color: es el *sistema* que no sirve, gane quien gane. Por eso aquí cabemos todos, vengas de donde vengas. "
     "Nos une lo que todos queremos: que lo básico funcione. ¿De acuerdo? Confirma tu Pulso de hoy. 👍"),

    (["cuesta", "gratis", "pagar", "cuota", "dinero", "precio", "donar", "donacion"],
     "Es *gratis*, y siempre lo será. 💜 Omnicracia no te cobra nada ni te pide cuota. "
     "Lo que te pedimos no es dinero: es que te informes, traigas a 3 y no te apagues. Eso vale más que cualquier donativo. 🔥"),

    (["seguro", "privacidad", "datos", "me espian", "peligro", "me pueden", "represalia"],
     "Tranquil@: todo lo que hacemos es *público, pacífico y legal* — esa es nuestra armadura. No pedimos nada raro ni compartimos tus datos. "
     "Y la fuerza está en ser *tantos* que no se atrevan. Solos nos aíslan; juntos somos intocables. 💜"),

    (["organizar", "mi ciudad", "mi estado", "empezar", "no hay nadie", "por donde", "como ayudo", "como le hago", "que hago"],
     "🔥 Esas ganas de mover tu lugar son EXACTAMENTE lo que necesita el país. Y no empiezas de cero.\n\n"
     "Tu plan, hoy mismo:\n"
     "1️⃣ No te apagues: confirma tu Pulso diario (el botón de cada día).\n"
     "2️⃣ Trae a 3 que de verdad estén hartos.\n"
     "3️⃣ Cae a la junta del miércoles 9 PM y propón.\n\n"
     "El que da el primer paso se vuelve el referente de su gente. ¿Vas a ser tú? 💜"),

    (["convencer", "convenzo", "mi familia", "mis amigos", "como les digo", "manual"],
     "¡Me encanta que quieras sumar — eres de los valiosos! 🔥 3 claves:\n\n"
     "1️⃣ No discutas de partidos. Toca el dolor que YA sienten: \"¿no te harta pagar impuestos y que nada sirva?\". Ahí todos dicen que sí.\n"
     "2️⃣ Dales esperanza: \"hay casi medio millón organizándonos, sin partido, pacífico y legal — y es gratis\".\n"
     "3️⃣ Pídeles algo chiquito: \"entra nada más a ver\".\n\n"
     "Copia y manda esto 👉 _\"Me uní a Omnicracia: casi medio millón sin partido, pacífico y legal, para que el país funcione. Entra: omnicracia.com\"_"),

    (["plan", "cronograma", "paso a paso", "como se cambia", "como lo van a lograr", "estrategia"],
     "Aquí SÍ hay plan, no solo quejas. 💜 Va en orden:\n\n"
     "1️⃣ Le quitamos el poder a TODOS los políticos, pacífica y legalmente: con la unión de la mayoría dejamos de sostener a quienes abusan.\n"
     "2️⃣ El país no se cae: los servicios siguen con los trabajadores profesionales de siempre, ahora supervisados por los ciudadanos.\n"
     "3️⃣ Nominaciones ciudadanas: la gente propone a los mejores perfiles, se evalúan por capacidad, valores y honestidad, y entre esos, elegimos.\n"
     "4️⃣ Cada responsable se califica cada mes. Si no cumple, se va. Castigo inmediato.\n\n"
     "Todo pacífico y dentro de la ley. ¿Le entras? 🔥"),

    (["revocacion", "firmar", "firma", "ine", "mandato"],
     "La revocación de mandato es un *derecho* tuyo en la Constitución (Art. 35): a mitad del sexenio, el pueblo decide si el que gobierna se queda o se va. "
     "La firma oficial se hace en la app del INE cuando abra la ventana; nosotros nos organizamos para llegar en masa el primer día.\n\n"
     "Regístrate ya 👉 " + LINKS["revocacion"] + "\nEl que se organiza antes, gana. ✍️"),

    (["revocacion no", "deja igual", "congreso pone", "no sirve la revocacion", "ponen a otro"],
     "Tienes razón, y qué bueno que lo sabes: la revocación por sí sola no basta, porque la ley deja que el relevo lo pongan los mismos.\n\n"
     "Por eso en Omnicracia la revocación *NO es el final*: es un ejercicio de *unificación* para juntarnos y medir nuestra fuerza. De ahí salen dos caminos, y los dos nos convienen:\n"
     "• Si se logra, surfeamos la ola y los quitamos a todos de un golpe.\n"
     "• Si no, ya juntamos a un montón de gente lista para la siguiente acción.\n\n"
     "El objetivo real no es cambiar una silla: es cambiar el sistema entero, pacífica y legalmente. 💜"),

    (["como se elige", "como se eligen", "como se quita", "como quitan", "nominacion", "quien gobierna"],
     "Cambiamos el sistema de *POPULARIDAD* por uno de *FUNCIONALIDAD*:\n\n"
     "• No gana el más conocido ni el que más gastó. Gana el más *capaz y honesto*.\n"
     "• Los ciudadanos nominan buenos perfiles; se evalúan con una plataforma independiente: trayectoria, valores, honestidad, capacidad.\n"
     "• De entre los mejores de cada lugar, los ciudadanos eligen.\n"
     "• Y cada mes se les califica. ¿No cumplen? Se van.\n\n"
     "Elegido por capacidad, vigilado siempre, castigado al instante si falla. Eso sí sirve. 💜"),

    (["si no estas", "fundador", "depende de una persona", "continuidad", "y si te pasa algo", "si matan"],
     "La mejor pregunta, y la respuesta es nuestro seguro de vida: esto *NO depende de una sola persona*. "
     "El día que todos nos sabemos el plan, nadie es indispensable — ni el fundador. Si alguien quisiera parar esto quitando a alguien, no le serviría: todos seguimos el mismo plan.\n\n"
     "Por eso lo más valiente que puedes hacer es informarte y pasar la estafeta. Entre más gente sepa, más imparable. ¿Te sumas a que seamos tantos que ya nadie lo pueda parar? 🔥"),

    (["junta", "reunion", "zoom", "miercoles", "liga"],
     "📅 La junta nacional es *cada MIÉRCOLES 9 PM* (hora CDMX) por Zoom. Ahí nos sincronizamos y decidimos juntos.\n\n"
     "Liga 👉 " + LINKS["zoom"] + "\n(Meeting ID 898 6603 3549)\n\nPon la alarma y trae a 3. Los que llegan, mueven el país. 🔥"),

    (["aportar", "talento", "memes", "camara", "editar", "diseno", "ayudar con", "escuadron", "voluntario"],
     "🙌 ¡Así se habla! Aquí nadie sobra. Memes, cámara, edición, diseño, voz, organización — todo suma.\n\n"
     "Únete al Escuadrón de creadores aquí 👉 https://chat.whatsapp.com/CeJequyScLk8p87lBC0jGr\n"
     "Tu talento multiplica el mensaje. ¿Con qué sumas tú? 🔥"),

    (["mujer", "mujeres", "equidad", "feminista", "genero"],
     "En Omnicracia cabemos todos por igual — mujeres y hombres, codo a codo. Aquí no sobra nadie y no falta nadie; la fuerza es de todos. "
     "De hecho, muchas de las que más mueven sus estados son mujeres. 💜 ¿Te sumas con tu gente?"),

    (["efectivo", "dinero digital", "me controlen", "me quiten mi dinero", "ley digital", "banco"],
     "Te entiendo, y ese miedo es real y válido — es justo la clase de abuso que nos tiene hartos. 😤\n\n"
     "No soy quién para decirte qué hacer con tu dinero (para eso, alguien de tu confianza en finanzas). Pero sí te digo esto: "
     "el día que deciden por ti sin consultarte es porque estamos desorganizados y callados. Juntos, ponemos límites. "
     "¿Te sumas a los que sí ponen el alto? 💜"),

    (["noticia", "mañanera", "presidente", "presidenta", "claudia", "amlo", "opinas", "que opinas"],
     "Aquí no nos casamos con ningún color ni nos peleamos por el tema del día — ese es el juego que nos divide. "
     "Nosotros vemos el fondo: el sistema no sirve, gane quien gane. Y eso solo lo cambia la gente organizada. "
     "¿Te sumas a lo que sí mueve la aguja? 💜"),
]
