package OOP;
import java.util.Set;

public class NumberSearch {
    static final int NUMBER_OF_PLAYERS = 10; 
    static final int NUMBER_OF_BOXES = 10; 
    static final int OPEN_LIMIT = 5; 
    public static void main(String[] args) {
        
        // FollowNumberInBox followNumberInBox = new FollowNumberInBox();
        // followNumberInBox

        Game game = new Game(NUMBER_OF_PLAYERS, NUMBER_OF_BOXES, OPEN_LIMIT);

        game.printBoxes();
        game.printPlayers();
        // Room ruum = new Room(10);

        // Player playa = new Player(8);

        // ruum.getBoxes()[6].openBox();
        // ruum.getBoxes()[8].openBox();


        
        
    }
}
