import pygame
import random
import sys

# تهيئة Pygame
pygame.init()

# الإعدادات الأساسية
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# الألوان
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# إنشاء الشاشة
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("مغامرة الفضاء - Space Adventure")
clock = pygame.time.Clock()

# كلاس السفينة اللاعب
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 40))
        self.image.fill(BLUE)
        pygame.draw.polygon(self.image, WHITE, [(25, 0), (0, 40), (50, 40)])
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 10
        self.speed = 5
        self.lives = 3

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

# كلاس الرصاص
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((4, 10))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed = -10

    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom < 0:
            self.kill()

# كلاس الأعداء
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 30))
        self.image.fill(RED)
        pygame.draw.polygon(self.image, WHITE, [(20, 0), (0, 30), (40, 30)])
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(-100, -40)
        self.speed = random.randint(1, 3)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

# كلاس النقاط
class Score:
    def __init__(self):
        self.score = 0
        self.font = pygame.font.Font(None, 36)

    def update(self, points):
        self.score += points

    def draw(self, screen):
        text = self.font.render(f"النقاط: {self.score}", True, WHITE)
        screen.blit(text, (10, 10))
        lives_text = self.font.render(f"الأرواح: {player.lives}", True, WHITE)
        screen.blit(lives_text, (10, 50))

# المتغيرات الرئيسية
all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
enemies = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

score = Score()
running = True
enemy_timer = 0

# الموسيقى والأصوات (اختيارية)
# pygame.mixer.music.load("background.mp3")
# pygame.mixer.music.play(-1)

while running:
    clock.tick(FPS)
    
    # معالجة الأحداث
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    # تحديث الكائنات
    all_sprites.update()
    
    # إضافة أعداء جدد
    enemy_timer += 1
    if enemy_timer > 30:  # كل ثانية تقريباً
        enemy = Enemy()
        all_sprites.add(enemy)
        enemies.add(enemy)
        enemy_timer = 0

    # التصادم بين الرصاص والأعداء
    hits = pygame.sprite.groupcollide(enemies, bullets, True, True)
    for hit in hits:
        score.update(10)

    # التصادم بين اللاعب والأعداء
    if pygame.sprite.spritecollideany(player, enemies):
        player.lives -= 1
        if player.lives <= 0:
            running = False

    # رسم كل شيء
    screen.fill(BLACK)
    all_sprites.draw(screen)
    score.draw(screen)

    # شاشة النهاية
    if player.lives <= 0:
        font = pygame.font.Font(None, 74)
        text = font.render("انتهت اللعبة!", True, RED)
        text_rect = text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
        screen.blit(text, text_rect)
        
        score_text = score.font.render(f"النقاط النهائية: {score.score}", True, WHITE)
        score_rect = score_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 60))
        screen.blit(score_text, score_rect)

    pygame.display.flip()

pygame.quit()
sys.exit()