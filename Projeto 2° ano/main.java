import java.util.Scanner;

public class main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Digite a temperatura em Celsius (°C): ");
        while (!sc.hasNextDouble()) {
            System.out.println("Entrada inválida. Digite um número.");
            sc.next();
            System.out.print("Digite a temperatura em Celsius (°C): ");
        }
        double celsius = sc.nextDouble();
        double fahrenheit = (celsius * 9.0 / 5.0) + 32.0;
        double kelvin = celsius + 273.15;

        System.out.printf("Temperatura em Celsius: %.1f °C%n", celsius);
        System.out.printf("Temperatura em Fahrenheit: %.1f °F%n", fahrenheit);
        System.out.printf("Temperatura em Kelvin: %.2f K%n", kelvin);

        sc.close();
    }
}