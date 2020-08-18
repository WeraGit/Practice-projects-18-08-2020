//Weronika 18/08/2020

public class Magic8 {

  public static void main(String[] args) {
    int randNum = (int) (Math.random() * 20 + 1);

    System.out.println("Just think of a question that can be answered \"Yes\" or \"No\", concentrate very, very hard...\n\n\nMagic 8-Ball says: \n");     

    if (randNum == 1) {
      System.out.println("It is certain.");
    } else if (randNum == 2) {
      System.out.println("It is decidedly so.");
    } else if (randNum == 3) {
      System.out.println("Without a doubt.");      
    } else if (randNum == 4) {      
      System.out.println("Yes - definitely.");      
    } else if (randNum == 5) {      
      System.out.println("You may rely on it.");      
    } else if (randNum == 6) {      
      System.out.println("As I see it, yes.");      
    } else if (randNum == 7) {
      System.out.println("Most likely.");      
    } else if (randNum == 8) {      
      System.out.println("Outlook good.");      
    } else if (randNum == 9) {      
      System.out.println("Yes.");      
    } else if (randNum == 10) {      
      System.out.println("Signs point to yes.");      
    } else if (randNum == 11) {      
      System.out.println("Reply hazy, try again.");      
    } else if (randNum == 12) {
      System.out.println("Ask again later.");      
    } else if (randNum == 13) {
      System.out.println("Better not tell you now.");      
    } else if (randNum == 14) {      
      System.out.println("Cannot predict now.");
    } else if (randNum == 15) {
      System.out.println("Concentrate and ask again.");      
    } else if (randNum == 16) {      
      System.out.println("Don't count on it.");      
    } else if (randNum == 17) {      
      System.out.println("My reply is no.");
    } else if (randNum == 18) {
      System.out.println("My sources say no.");
    } else if (randNum == 19) {
      System.out.println("Outlook not so good.");
    } else {  //one option left - random number being 20
      System.out.println("Very doubtful.");      
    }

    //Switch option would look like this:
    // switch (randNum) {
    //   case 1:
    //     System.out.println("It is certain.");
    //     break;
    //   case 2:
    //     System.out.println("It is decidedly so.");
    //     break;
    //   case 3:
    //     System.out.println("Without a doubt.");
    //     break;      
    //   case 4:
    //     System.out.println("Yes - definitely.");
    //     break;
    //   case 5:
    //     System.out.println("You may rely on it.");   
    //     break;   
    //   case 6:  
    //     System.out.println("As I see it, yes.");
    //     break;      
    //   case 7:
    //     System.out.println("Most likely.");
    //     break;
    //     ....
    //   case 20:
    //     System.out.println("Very doubtful.");
    //     break;
    //   default:
    //     System.out.println("Answer not found");
    // }

  }
}