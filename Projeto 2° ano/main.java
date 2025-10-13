import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Atividade 01 - Simulando um sistema escolar");
        System.out.println("Informe 8 notas (duas notas por bimestre):");

        double[] notas = new double[8];
        for (int i = 0; i < 8; i++) {
            System.out.printf("Nota %d: ", i + 1);
            while (!sc.hasNextDouble()) {
                System.out.print("Valor inválido. Digite um número: ");
                sc.next();
            }
            notas[i] = sc.nextDouble();
        }

        double b1 = (notas[0] + notas[1]) / 2.0;
        double b2 = (notas[2] + notas[3]) / 2.0;
        double b3 = (notas[4] + notas[5]) / 2.0;
        double b4 = (notas[6] + notas[7]) / 2.0;

        double s1 = (b1 + b2) / 2.0;
        double s2 = (b3 + b4) / 2.0;

        double mediaFinal = (s1 + s2) / 2.0;

        System.out.println("\nPráticas\n");
        System.out.printf("1o Bimestre: %.1f%n", b1);
        System.out.printf("2o Bimestre: %.1f%n", b2);
        System.out.printf("1o Semestre: %.1f%n", s1);
        System.out.println("----------------------");
        System.out.printf("3o Bimestre: %.1f%n", b3);
        System.out.printf("4o Bimestre: %.1f%n", b4);
        System.out.printf("2o Semestre: %.1f%n", s2);
        System.out.println("-----------------------");
        System.out.printf("Média Final: %.1f%n", mediaFinal);

        sc.close();
    }
}
