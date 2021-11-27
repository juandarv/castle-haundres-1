@namespace
class SpriteKind:
    subdito = SpriteKind.create()
    objeto = SpriteKind.create()

def on_on_zero(status):
    statusbar2.sprite_attached_to().destroy()
statusbars.on_zero(StatusBarKind.health, on_on_zero)

def on_overlap_tile(sprite, location):
    global fantasma
    rey.set_position(25, 25)
    tiles.set_tilemap(tilemap("""
        level5
    """))
    fantasma = sprites.create(img("""
            ........................
                    ........................
                    ........................
                    ........................
                    ..........ffff..........
                    ........ff1111ff........
                    .......fb111111bf.......
                    .......f11111111f.......
                    ......fd11111111df......
                    ......fd11111111df......
                    ......fddd1111dddf......
                    ......fbdbfddfbdbf......
                    ......fcdcf11fcdcf......
                    .......fb111111bf.......
                    ......fffcdb1bdffff.....
                    ....fc111cbfbfc111cf....
                    ....f1b1b1ffff1b1b1f....
                    ....fbfbffffffbfbfbf....
                    .........ffffff.........
                    ...........fff..........
                    ........................
                    ........................
                    ........................
                    ........................
        """),
        SpriteKind.enemy)
    game.show_long_text("se libero el fantasma", DialogLayout.BOTTOM)
    fantasma.vx += 100
    fantasma.vy += 100
    fantasma.set_bounce_on_wall(True)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.stair_east,
    on_overlap_tile)

def on_overlap_tile2(sprite2, location2):
    tiles.set_tilemap(tilemap("""
        level8
    """))
    rey.set_position(25, 25)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.collectible_red_crystal,
    on_overlap_tile2)

def on_overlap_tile3(sprite3, location3):
    game.over(True)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.door_open_north,
    on_overlap_tile3)

def on_overlap_tile4(sprite4, location4):
    rey.set_position(25, 25)
    tiles.set_tilemap(tilemap("""
        level3
    """))
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.stair_south,
    on_overlap_tile4)

def on_on_overlap(sprite5, otherSprite):
    statusbars.get_status_bar_attached_to(StatusBarKind.health, rey).value += -100
    fantasma.destroy()
    game.over(False)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap)

fantasma: Sprite = None
statusbar2: StatusBarSprite = None
rey: Sprite = None
scene.set_background_image(assets.image("""
    hola
"""))
rey = sprites.create(img("""
        . . . . . 5 f 5 5 f 5 . . . . .
            . . . . e 5 5 2 2 5 5 e . . . .
            . . . e 6 8 2 5 5 2 8 6 e . . .
            . . e 6 5 5 5 5 5 5 5 5 6 e . .
            . . 6 4 4 2 2 2 2 2 2 4 4 6 . .
            . . e 4 2 8 8 8 8 8 8 2 4 e . .
            . . e 8 8 8 e e e e 8 8 8 e . .
            . e e 4 e b f 4 4 f b e 4 e e .
            . e 4 4 4 1 7 d d 7 1 4 4 4 e .
            . . e 4 4 d e e e e d 4 4 e . .
            . . 7 7 4 4 4 e e 4 4 4 7 7 . .
            . . 7 4 4 2 9 2 2 9 2 4 4 7 . .
            . . 4 d d 6 9 9 9 9 6 d d 4 . .
            . . 4 4 d 6 9 8 8 9 6 d 4 4 . .
            . . . . . 6 6 6 6 6 6 . . . . .
            . . . . . 8 8 . . 8 8 . . . . .
    """),
    SpriteKind.player)
rey.set_position(80, 30)
subdito2 = sprites.create(img("""
        . . . . . . 8 8 8 8 . . . . . .
            . . . . 8 8 e e e e 8 8 . . . .
            . . . 8 e e e 8 8 e e e 8 . . .
            . . 8 8 8 8 8 2 2 8 8 8 8 8 . .
            . . 8 8 8 2 8 2 2 8 2 8 8 8 . .
            . . 8 8 2 8 2 8 8 2 8 2 8 8 . .
            . 8 8 8 8 2 2 e e 2 2 8 8 8 8 .
            . 8 8 e 8 2 8 8 8 8 2 8 e 8 8 .
            . 8 e e 8 8 e e e e 8 e e 8 8 .
            . . 8 e e e e e e e e e e 8 . .
            . . . 8 e e e e e e e e 8 . . .
            . . 6 6 8 8 8 8 8 8 8 8 6 6 . .
            . . 6 d 8 6 6 6 6 6 6 8 d 6 . .
            . . 4 4 8 4 4 4 4 4 4 8 4 4 . .
            . . . . . 9 9 9 9 9 9 . . . . .
            . . . . . 6 8 . . 8 6 . . . . .
    """),
    SpriteKind.subdito)
subdito2.set_position(80, 100)
animation.run_movement_animation(subdito2,
    animation.animation_presets(animation.fly_to_center),
    2000,
    False)
pause(2500)
game.show_long_text("rey: hola súbdito", DialogLayout.BOTTOM)
game.show_long_text("súbdito: hola rey tenemos un problema", DialogLayout.BOTTOM)
game.show_long_text("rey: que clase de problema", DialogLayout.BOTTOM)
game.show_long_text("súbdito: recuerdas el castillo donde vivías de pequeño ",
    DialogLayout.BOTTOM)
game.show_long_text("rey: que tiene que ver", DialogLayout.BOTTOM)
game.show_long_text("súbdito: lo que pasa es que hay rumores de que habían fantasmas y eso atemorizó a los campesinos",
    DialogLayout.BOTTOM)
pause(2000)
game.show_long_text("rey: voy a tratar de arreglarlo", DialogLayout.BOTTOM)
controller.move_sprite(rey)
rey.set_stay_in_screen(True)
statusbar2 = statusbars.create(20, 2, StatusBarKind.health)
statusbar2.attach_to_sprite(rey)
pause(100)
subdito2.destroy()
tiles.set_tilemap(tilemap("""
    level02
"""))
scene.camera_follow_sprite(rey)
rey.set_position(25, 25)