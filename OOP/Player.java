package OOP;
public class Player {
    private int number;

    public int getNumber() { return number; }

    public Player(int number) {
        this.number = number;
    }

    public void crackOpenAColdOne(int howMany) {
        System.out.println("Ooaaaahhhhh, that hits the spot!");
    }

    private boolean chooseNextBox(Room room) {
        return true;
    }

    public boolean findMyBox(Room room) {
        return true;
    }

    @Override
    public String toString() {
        return "Player number: " + number;
    }
}
