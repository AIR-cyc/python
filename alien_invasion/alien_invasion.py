# -*- coding: utf-8 -*-
#模块pygame包含开发游戏所需的功能
import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
#from alien import Alien
import game_functions as gf

def run_game():
    #初始化pygame、设置和屏幕对象
    pygame.init() #初始化背景设置，让pygame能够正确的工作
    ai_settings = Settings()
    #调用函数来创建一个名为screen的显示窗口
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)) 
    pygame.display.set_caption("Alien Invasion")
    
    #创建play按钮
    play_button = Button(ai_settings, screen, "Play")
    
     #创建存储游戏统计信息的实例，并创建记分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    #创建一艘飞船、一个子弹编组和一个外星人编组
    ship = Ship(ai_settings, screen)
    #创建一个用于存储子弹的编组
    bullets = Group()
    aliens = Group()
    #创建外星人人群
    gf.create_fleet(ai_settings, screen, ship, aliens)
    
    #开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button,
                        ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens,
                              bullets)
            #更新子弹后再更新外星人的位置，因为要检查是否有子弹撞到了外星人
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens,
                         bullets, play_button)

#初始化游戏并开始主循环        
run_game()