package OOP;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Random;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Room implements Cloneable {
    private Box[] boxes;
    
    public Box[] getBoxes() { return boxes; }

    Room () {
        int numberOfBoxes = 100;
        this.setupBoxes(numberOfBoxes);
    }

    Room (int numberOfBoxes) {
        this.setupBoxes(numberOfBoxes);
    }

    private void setupBoxes(int numberOfBoxes) {
        this.boxes = new Box[numberOfBoxes];

        ArrayList<Integer> undistributedHiddenNumbers = (ArrayList<Integer>) IntStream.rangeClosed(0, numberOfBoxes - 1).boxed().collect(Collectors.toList());
        Collections.shuffle(undistributedHiddenNumbers, new Random());

        for (int i = 0; i < numberOfBoxes; i++) {
            this.boxes[i] = new Box(i, undistributedHiddenNumbers.get(i));
        }
    }
}
