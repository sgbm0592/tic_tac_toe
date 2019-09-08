from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from . import tictactoe as game

class HomeView(View):
    def get(self, request):
        return render(request, 'game/index.html')

boardGame = [' '] * 9;
player = 'O'
computer = 'X'

class GameView(View):
    def get(self,request):
        global boardGame
        player_move = int(request.GET.get('move'))
        playing = True
        message = ' '
        game.make_move(boardGame, player, player_move)
        if not game.check_board_full(boardGame):
            move = game.get_computer_move(boardGame)
            game.make_move(boardGame, computer, move)
        else:
            move = -1

        if game.check_winner(boardGame, player):
            game.show_board(boardGame)
            message = 'You are the winner!'
            playing = False
        else:
            if game.check_board_full(boardGame):
                game.show_board(boardGame)
                message =  'Tie Game!'
                playing = False

        if game.check_winner(boardGame, computer):
            game.show_board(boardGame)
            message = 'You lose the game.'
            print(message)
            playing = False
        else:
            if game.check_board_full(boardGame):
                game.show_board(boardGame)
                message = 'The game is a tie!'
                playing = False

        data = {
            'computer_move': move,
            'playing': playing,
            'message' : message,
        }
        print(data)
        return JsonResponse(data)

class ReplayView(View):
    def get(self, request):
        global boardGame
        boardGame.clear()
        boardGame = [' '] * 9

        game.show_board(boardGame)
        return redirect(reverse('home'))