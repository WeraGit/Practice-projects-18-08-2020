//Weronika 18/08/2020

using System;

namespace ConsoleGame
{
  class Game : SuperGame
  {
    public new static void UpdatePosition(string key, out int xCoor, out int yCoor) {
      switch(key) {
        case "LeftArrow":
          xCoor = -1;
          yCoor = 0;
          break;
        case "RightArrow":
          xCoor = 1;
          yCoor = 0;
          break;
        case "UpArrow":
          xCoor = 0;
          yCoor = -1;
          break;
        case "DownArrow":
          xCoor = 0;
          yCoor = 1;
          break;
        default:
          xCoor = 0;
          yCoor = 0;
          break;
      }
    }

    public new static char UpdateCursor(string key) {
      if (key == "LeftArrow"){
        return '<';
      } else if (key == "RightArrow"){
        return '>';
      } else if (key ==  "UpArrow"){
        return '^';
      } else if (key == "DownArrow"){
        return 'v';
      } else {
        return '-';
      }
    }

    public new static int KeepInBounds(int coor, int maxValue) {
      if (coor < 0) {
        return (maxValue + coor);
      } else if (coor >= maxValue) {
        return (maxValue - coor);
      } else {
        return coor;
      }
    }

    public new static bool DidScore(int xChar, int yChar, int xFruit, int yFruit) {
      if (xChar == xFruit && yChar == yFruit){
        return true;
      } else {
        return false;
      }      
    }
    
    
  }
}
