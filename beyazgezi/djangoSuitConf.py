SUIT_CONFIG = {
    # header
     'ADMIN_NAME': 'Beyaz Gezi Yönetim Paneli',
    'HEADER_DATE_FORMAT': ' j F Y - l',
    # 'HEADER_TIME_FORMAT': 'H:i',

    # forms
    # 'SHOW_REQUIRED_ASTERISK': True,  # Default True
    # 'CONFIRM_UNSAVED_CHANGES': True, # Default True

    # menu
    #'SEARCH_URL': '/admin/auth/user/',
    'SEARCH_URL': '',
    'MENU_ICONS': {
        'bilgiler': 'icon-info-sign',
        'fotograflar': 'icon-camera',
        'iletisim': 'icon-envelope',
        'sayfalar':'icon-file',
        'yazilar':'icon-pencil',
        'auth': 'icon-lock',
     },
     #'MENU_OPEN_FIRST_CHILD': True, # Default True
    #'MENU_EXCLUDE': ('auth.group',),
    # 'MENU': (
    #     'sites',
    #     {'app': 'auth', 'icon':'icon-lock', 'models': ('user', 'group')},
    #     {'label': 'Settings', 'icon':'icon-cog', 'models': ('auth.user', 'auth.group')},
    #     {'label': 'Support', 'icon':'icon-question-sign', 'url': '/support/'},
    # ),

    # misc
    'LIST_PER_PAGE': 20
}