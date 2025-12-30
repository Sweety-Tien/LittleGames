import unittest
from LittleGames import CardUtils as poker
from LittleGames import Deck

class TestHalfTenPoker(unittest.TestCase):

    def test_point_number_cards(self):
        self.assertEqual(poker.point(2), 2)
        self.assertEqual(poker.point(10), 10)

    def test_point_face_cards_are_half(self):
        # J, Q, K 都應該是 0.5
        self.assertEqual(poker.point(11), 0.5)
        self.assertEqual(poker.point(12), 0.5)
        self.assertEqual(poker.point(13), 0.5)

    def test_check_not_burst(self):
        self.assertTrue(poker.check(10.5))

    def test_check_burst(self):
        self.assertFalse(poker.check(10.6))

class TestDeck(unittest.TestCase):

    def test_draw_unique_cards(self):
        deck = Deck()
        drawn = [deck.draw() for _ in range(52)]
        self.assertEqual(len(drawn), 52)
        self.assertEqual(len(set(drawn)), 52)

    def test_draw_empty_deck_raises(self):
        deck = Deck()
        for _ in range(52):
            deck.draw()
        with self.assertRaises(IndexError):
            deck.draw()

from LittleGames import GameState

class TestGameState(unittest.TestCase):

    def test_player_bust(self):
        state = GameState()
        state.add_player_card(10)
        state.add_player_card(1)
        self.assertTrue(state.is_player_bust())

    def test_player_not_bust(self):
        state = GameState()
        state.add_player_card(5)
        state.add_player_card(5.5)
        self.assertFalse(state.is_player_bust())

    def test_five_cards_win(self):
        state = GameState()
        for _ in range(5):
            state.add_player_card(1)
        self.assertTrue(state.is_player_five_cards())
        self.assertTrue(state.is_game_over())

    def test_banker_should_draw(self):
        state = GameState()
        state.add_banker_card(7)
        self.assertTrue(state.banker_should_draw())
        state.add_banker_card(0.5)
        self.assertFalse(state.banker_should_draw())

    def test_decide_winner_player_win(self):
        state = GameState()
        state.sum_player = 8
        state.sum_banker = 7
        self.assertIn('玩家獲勝', state.decide_winner())

    def test_decide_winner_draw(self):
        state = GameState()
        state.sum_player = 8
        state.sum_banker = 8
        state.player_cards = 2
        state.banker_cards = 2
        self.assertIn('和局', state.decide_winner())



if __name__ == "__main__":
    unittest.main()
