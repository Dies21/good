import pygame
import random
import pygame_menu
import pygame.time

pygame.init()
screen = pygame.display.set_mode((1400, 1000))
pygame.display.set_caption("Random RPG")
surface = pygame.display.set_mode((1200, 800))



sound_click = pygame.mixer.Sound('resources\\click.mp3')
sound_background_music = pygame.mixer.Sound('resources\\background_music.mp3')


names = ["Даня Геракл", "Ярик Ахиллес", "Андрей Бабайка", "Максим Змея", "Остап Свинья", 
  "Оливье-Жюй да Глотай", "Дима Зевс", "", "Джеймс Леброн", "Фил Фаст"]
places = ["грязной деревне", "богатом городе", "бедной семье", "богатой семье", "крепости", "замке", "лесу", "горах"]

funny_stories = [
    "Однажды в далекой деревне жил-был смешной клоун. Он всегда шутил и делал \nлюдей смеяться. Однажды он так смешно подскользнулся на банановой кожуре, что все жители деревни не могли перестать\n смеяться целый день.",
    "В одном замке жил великий маг, который был известен своими \nстранными экспериментами. Однажды он случайно превратил свою кошку в дракона,\n и теперь она заправляла весь замок.",
    "Однажды магический эльф нашел волшебную флейту, которая \nзаставляла всех, кто ее слушал, начинать танцевать. Он решил устроить вечеринку для всех своих друзей и сыграл \nна флейте. \nВесь лес наполнился танцующими животными и смехом.",
    "Храбрый рыцарь отправился в поисках золотого яйца, о котором \nслышал в легендах. Он нашел гигантского петуха, который охранял яйцо. Но когда рыцарь взял яйцо в руки, оказалось, \nчто оно было обычным куриным яйцом, только большого размера."]

def draw_text(text, font_size, x, y, color):
    font = pygame.font.Font(None, font_size)
    lines = text.split('\n')  # Split the text into lines using line breaks
    line_height = font.get_linesize()  # Get the height of each line

    for i, line in enumerate(lines):
        text_surface = font.render(line, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y + i * line_height)  # Adjust the y-coordinate for each line
        screen.blit(text_surface, text_rect)



def display_funny_story():
    story = random.choice(funny_stories)
    draw_text(story, 35, 1200//2, 800//2 - 200,  (0, 255, 0))

def set_difficulty(value, difficulty):
    # Do the job here !
    pass

def display_funny_story():
    new_story = random.choice(funny_stories)
    draw_text(new_story, 35, 1200//2, 800//2 - 200, (0, 255, 0))
    print("random story")
    pygame.display.flip()  # Upda


def start_the_game():
    sound_click.play() 
    #sound_background_music.stop()
    sound_background_music.play()
    
    menu.disable() 
    pygame.time.Clock().tick(60)  # Limit the screen refresh rate to 60 frames per second
    backgrounds = ["resources/1.jpg",  "resources/3.jpg"]
    background_image_choice = random.choice(backgrounds)
    background_image = pygame.image.load(background_image_choice).convert()
    background_image = pygame.transform.scale(background_image, (1200, 800))
    screen.blit(background_image, [0, 0])
    name = random.choice(names)
    place = random.choice(places)
    draw_text("Добро пожаловать в наш мир драконов и магов-алкоголиков", 35, 1200//2, 800//2 - 200, (255, 255, 255))
    draw_text(f"Тебя зовут {name}, и ты родился в {place}.", 35, 1200//2, 800//2, (255, 255, 255))
    
    pygame.display.flip()  # Update the screen after drawing the welcome text
    pygame.time.wait(5000)  # Delay for 5 seconds (5000 milliseconds)
    
    for _ in range(5):
        screen.blit(background_image, [0, 0])  # Clear the screen before showing the funny story
        pygame.time.wait(500)
        display_funny_story()
        pygame.time.wait(10000)  # Delay for an additional 10 seconds (10000 milliseconds)
        pygame.event.get()  # Process events during the waiting period
        background_image_choice = random.choice(backgrounds)
        background_image = pygame.image.load(background_image_choice).convert()
        background_image = pygame.transform.scale(background_image, (1200, 800))

    pygame.display.flip()  # U

    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        pygame.display.flip()  # 

menu = pygame_menu.Menu('Welcome', 1200, 800,
                    theme=pygame_menu.themes.THEME_BLUE)

menu.add.text_input('Name :', default='Богдан Богатырь')
menu.add.selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(surface)
