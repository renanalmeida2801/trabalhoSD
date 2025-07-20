import java.io.IOException;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URI;
import java.net.URL;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.util.Locale;
import java.util.Scanner;

public class ClienteJava {
    private static final String BASE_URL = "http://localhost:8000";

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int opcao;

        do {
            System.out.println("\n=== MENU CLIENTE JAVA ===");
            System.out.println("1. Cadastrar produto");
            System.out.println("2. Listar produtos");
            System.out.println("3. Sair");
            System.out.print("Escolha uma opção: ");
            opcao = scanner.nextInt();
            scanner.nextLine(); // Limpar buffer

            switch (opcao) {
                case 1 -> cadastrarProduto(scanner);
                case 2 -> listarProdutos();
                case 3 -> System.out.println("Encerrando cliente...");
                default -> System.out.println("Opção inválida. Tente novamente.");
            }

        } while (opcao != 3);
    }

    private static void cadastrarProduto(Scanner scanner) {
        try {
            System.out.print("Nome: ");
            String nome = scanner.nextLine();

            System.out.print("Fabricante: ");
            String fabricante = scanner.nextLine();

            System.out.print("Preço: ");
            double preco = scanner.nextDouble();

            System.out.print("Quantidade: ");
            int quantidade = scanner.nextInt();
            scanner.nextLine(); // limpar buffer

            System.out.print("Tipo biológico (vacina): ");
            String tipoBiologico = scanner.nextLine();

            System.out.print("Validade (YYYY-MM-DD): ");
            String validade = scanner.nextLine();

            String json = String.format(Locale.US, """
            {
                "nome": "%s",
                "fabricante": "%s",
                "preco": %.2f,
                "quantidade": %d,
                "tipo_biologico": "%s",
                "validade": "%s"
            }
            """, nome, fabricante, preco, quantidade, tipoBiologico, validade);

            URL url = new URL(BASE_URL + "/produtos/vacina_perecivel");
            HttpURLConnection con = (HttpURLConnection) url.openConnection();
            con.setRequestMethod("POST");
            con.setRequestProperty("Content-Type", "application/json");
            con.setDoOutput(true);

            try (OutputStream os = con.getOutputStream()) {
                os.write(json.getBytes());
                os.flush();
            }

            int status = con.getResponseCode();
            System.out.println("Código de resposta: " + status);

            if (status == 200 || status == 201) {
                System.out.println("Produto cadastrado com sucesso.");
            } else {
                Scanner erro = new Scanner(con.getErrorStream()).useDelimiter("\\A");
                System.out.println("Erro ao cadastrar produto:");
                if (erro.hasNext()) System.out.println(erro.next());
            }

            con.disconnect();
        } catch (IOException e) {
            System.out.println("Erro: " + e.getMessage());
        }
    }

    private static void listarProdutos() {
        try {
            HttpClient client = HttpClient.newHttpClient();
            HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(BASE_URL + "/produtos/"))
                .GET()
                .build();

            HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

            System.out.println("\nResposta da API:");
            System.out.println(response.body());

        } catch (Exception e) {
            System.out.println("Erro ao listar produtos: " + e.getMessage());
        }
    }

}
