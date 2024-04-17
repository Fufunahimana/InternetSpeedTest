import flet as ft 
from TypewriterEffectControl import TypeWriterControl


def main(page:ft.Page):
    page.title ="TypeWriter Effect"
    page.window_width = 400
    page.window_height = 500
    page.bgcolor ="#333333"
    page.theme_mode = "dark"
    page.window_center()
    page.scroll ="always"
    page.update()
    
    some_random_text ='''
    ChatGPT, pour Chat Generative Pre-trained Transformer, est un prototype d'agent conversationnel (chatbot) utilisant l'intelligence artificielle, développé par OpenAI et spécialisé dans le dialogue. Il est basé sur les grands modèles de langage d'OpenAI GPT-3.5 et GPT-4.
    ChatGPT est capable de répondre à des questions, de tenir des conversations, de générer du code informatique, et d'écrire, traduire ou     synthétiser des textes. Il peut le faire en tenant compte du contexte, et de contraintes telles que le style d'écriture. Les abonnements     payants (ChatGPT « Plus », « Team » et « Enterprise ») donnent accès au modèle plus avancé GPT-4 ainsi qu'à des agents conversationnels     spécialisés, et permettent l'analyse et la génération d'images.    
    GPT-3.5, qui est disponible gratuitement, a connaissance des événements survenus jusqu'en janvier 2022 ; là où les connaissances du modèle     payant GPT-4 s'arrêtent en avril 20232.
    
    En raison de ses multiples capacités, le prototype suscite des inquiétudes quant aux risques de détournement à des fins malveillantes, de     plagiat dans le monde universitaire et de suppressions d'emplois dans certains secteurs. ChatGPT soulève également des préoccupations en     matière de sécurité et de désinformation, car le modèle peut être utilisé pour créer des textes faux et des informations trompeuses.    
    Lancé en novembre 2022 dans une version gratuite et non connectée à Internet, ChatGPT bénéficie d’une large exposition médiatique et reçoit     un accueil globalement positif, bien que son exactitude factuelle soit critiquée. En janvier 2023, ChatGPT compte plus de 100 millions de     comptes enregistrés, et la société OpenAI est alors valorisée à 29 milliards de dollars américains3.    
    '''
    
    page.add(
        TypeWriterControl(some_random_text)
    )
    
    
    pass
ft.app(target=main)
