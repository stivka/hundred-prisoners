package OOP;

public class Game {
	private Room room;
	private Player[] players;
	private int openLimit;
    
	public Player[] getPlayers() { return players; }

	public Game(int numberOfBoxes, int numberOfPlayers, int openLimit) {
		this.room = new Room(numberOfBoxes);
		this.players = new Player[numberOfPlayers];
		this.openLimit = openLimit;

		for (int i = 0; i < numberOfPlayers; i++) { this.players[i] = new Player(i); }
	}
	
	public Game() {
		this.room = new Room(100);
		this.players = new Player[100];
		this.openLimit = 50;
		
		for (int i = 0; i < 100; i++) { this.players[i] = new Player(i); }
	}

	public Game(int scale) {
		this.room = new Room(scale);
		this.players = new Player[scale];
		this.openLimit = scale / 2;

		for (int i = 0; i < scale; i++) { this.players[i] = new Player(i); }
	}

	public void printBoxes() {
		for (Box box : room.getBoxes()) {
            System.out.println(box.toString());
        }
	}

	public void printPlayers() {
		for (Player player : players) {
            System.out.println(player.toString());
        }
	}

	public boolean runGame() {
		for (Player player : players) {
			player.findMyBox(this.room.clone());
		}
		return true;
	}
	
}
