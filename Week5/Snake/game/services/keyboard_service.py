import pygame
from game.shared.point import Point


class KeyboardService:
    """Detects player input. 
    
    The responsibility of a KeyboardService is to indicate whether or not a key is up or down.

    Attributes:
        _keys (Dict[string, int]): The letter to key mapping.
    """

    def __init__(self):
        """Constructs a new KeyboardService."""
        self._keys = {}
        
        self._keys['w'] = pygame.KEY_W
        self._keys['a'] = pygame.KEY_A
        self._keys['s'] = pygame.KEY_S
        self._keys['d'] = pygame.KEY_D

        self._keys['i'] = pygame.KEY_I
        self._keys['j'] = pygame.KEY_J
        self._keys['k'] = pygame.KEY_K
        self._keys['l'] = pygame.KEY_L

    def is_key_up(self, key):
        """Checks if the given key is currently up.
        
        Args:
            key (string): The given key (w, a, s, d or i, j, k, l)
        """
        pygame_key = self._keys[key.lower()]
        return pygame.is_key_up(pygame_key)

    def is_key_down(self, key):
        """Checks if the given key is currently down.
        
        Args:
            key (string): The given key (w, a, s, d or i, j, k, l)
        """
        pygame_key = self._keys[key.lower()]
        return pygame.is_key_down(pygame_key)