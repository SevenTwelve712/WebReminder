from page_making.classes.instructions import *
from page_making.finished_structures.navigation_bar_F import navbar_f


i = Instruction('html_reminder', [])
i.open_p()
i.plain_text('Перед тем, как начать, определимся с некоторыми терминами:')
i.close_p()
i.open_ul()
i.li('Тег — основная хуйня в html. Используется для разметки страниц')
i.li()