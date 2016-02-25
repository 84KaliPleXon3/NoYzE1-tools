import java.util.Random;

public class Hash {

	static Random random = new Random();
	static char[] list = { '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f' };

	public static void main(String[] yolo) {
		gen_hash();
	}

	static void gen_hash() {

		for (int i = 0; i < 32; i++) {
			System.out.print(list[random.nextInt(16)]);
		}
		System.out.println();
	}

}
