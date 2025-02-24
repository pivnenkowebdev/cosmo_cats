import pygame as pg
import time
from sprite_game import *

def dialogue_mode(sprite, text):
    sprite.update()
    screen.blit(space, (0, 0))
    screen.blit(sprite.image, sprite.rect)

    text1 = f1.render(text[text_number], True, pg.Color('white'))
    screen.blit(text1, (280, 450))

    if text_number < len(text) - 1:
        text2 = f1.render(text[text_number + 1], True, pg.Color('white'))
        screen.blit(text2, (280, 480))



pg.init()
pg.mixer.init()

size = (800, 600)
screen = pg.display.set_mode(size)
pg.display.set_caption("Космические коты")

FPS = 120
clock = pg.time.Clock()

is_running = True
mode = "start_scene"

meteorites = pg.sprite.Group()
mice = pg.sprite.Group()
lasers = pg.sprite.Group()

space = pg.image.load('Космические коты - фон.png').convert()
space = pg.transform.scale(space, size)

text_number = 0
f1 = pg.font.Font('Космические коты - шрифт.otf', 25)

captain = Captain()
alien = Alien()

start_text = ["Мы засекли сигнал с планеты Мур.",
              "",
              "Наши друзья, инопланетные коты,",
              "нуждаются в помощи.",
              "Космические мыши хотят съесть их луну,",
              "потому что она похожа на сыр.",
              "Как долго наш народ страдал от них, ",
              "теперь и муряне в беде...",
              "Мы должны помочь им.",
              "Вылетаем прямо сейчас.",
              "Спасибо, что починил звездолёт, штурман. ",
              "Наконец-то функция автопилота работает.",
              "Поехали!"]

alien_text = ["СПАСИТЕ! МЫ ЕЛЕ ДЕРЖИМСЯ!",
              "",
              "Мыши уже начали грызть луну...",
              "Скоро куски луны будут падать на нас.",
              "Спасите муриан!", ]

final_text = ["Огромное вам спасибо,",
              "друзья с планеты Мяу!",
              "Как вас называть? Мяуанцы? Мяуриане?",
              "В любом случае, ",
              "теперь наша планета спасена!",
              "Мы хотим отблагодарить вас.",
              "Капитан Василий и его штурман получают",
              "орден SKYSMART.",
              "А также несколько бутылок нашей",
              "лучшей валерьянки.",
              "",
              ""]



while is_running:

    # СОБЫТИЯ
    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_running = False
        if event.type == pg.KEYDOWN:
            if mode == 'start_scene':
                text_number += 2
                if text_number > len(start_text):
                    text_number = 0
                    mode = 'meteorites'

            if mode == 'alien_scene':
                text_number += 2
                if text_number > len(alien_text):
                    alien.rect.topleft = (-30, 600)
                    alien.mode = "up"
                    text_number = 0
                    mode = 'moon'

            if mode == 'final_scene':
                text_number += 2
                if text_number > len(final_text):
                    text_number = 0
                    mode = 'end'




    # ОБНОВЛЕНИЯ
    if mode == "start_scene":
        dialogue_mode(captain, start_text)



    if mode == "meteorites":
        ...

    if mode == "alien_scene":
        dialogue_mode(alien, alien_text)

    if mode == "moon":
        ...

    if mode == "final_scene":
        dialogue_mode(alien, final_text)

    pg.display.flip()
    clock.tick(FPS)
