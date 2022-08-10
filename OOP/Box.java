package OOP;
public class Box {
    private int label;
    private int hiddenNumber;
    private boolean isOpen;
    
    Box (int label, int hiddenNumber) {
        this.label = label;
        this.hiddenNumber = hiddenNumber;
        this.isOpen = false;
    }

    public int getLabel() {
        return label;
    }

    public boolean isOpen() {
        return isOpen;
    }

    public int openBox() {
        this.isOpen = true;
        return this.hiddenNumber;
    }

    @Override
    public String toString() {
        return "Box " + label + " [" + hiddenNumber + "] is currently " + (isOpen ? "opened" : "closed");
    }
}
