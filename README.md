# rest api 

## run project 
python manage.py runserver

## API de Avaliação de Produtos

Esta é a documentação da API de Avaliação de Produtos, que permite a criação, leitura, atualização e exclusão de produtos, comentários e avaliações.

## Endpoints

---

## **Produtos**

### 1. Listar Produtos
- **Método**: `GET`
- **URL**: `/api/products/`
- **Descrição**: Retorna uma lista de todos os produtos cadastrados.
- **Resposta**:
    ```json
    [
        {
            "id": 1,
            "name": "Produto 1",
            "description": "Produto de exemplo",
            "price": 100.5,
            "stock": 30
        }
    ]
    ```

### 2. Criar Produto
- **Método**: `POST`
- **URL**: `/api/products/create/`
- **Descrição**: Cria um novo produto.
- **Body (JSON)**:
    ```json
    {
        "name": "Produto 1",
        "description": "Produto de exemplo",
        "price": 100.50,
        "stock": 30
    }
    ```
- **Resposta**:
    ```json
    {
        "id": 1,
        "name": "Produto 1",
        "description": "Produto de exemplo",
        "price": 100.5,
        "stock": 30
    }
    ```

### 3. Detalhar Produto
- **Método**: `GET`
- **URL**: `/api/products/{id}/`
- **Descrição**: Retorna os detalhes de um produto específico.
- **Resposta**:
    ```json
    {
        "id": 1,
        "name": "Produto 1",
        "description": "Produto de exemplo",
        "price": 100.5,
        "stock": 30
    }
    ```

### 4. Atualizar Produto
- **Método**: `PUT`
- **URL**: `/api/products/{id}/update/`
- **Descrição**: Atualiza as informações de um produto.
- **Body (JSON)**:
    ```json
    {
        "name": "Produto Atualizado",
        "description": "Descrição atualizada",
        "price": 150.75,
        "stock": 20
    }
    ```
- **Resposta**:
    ```json
    {
        "id": 1,
        "name": "Produto Atualizado",
        "description": "Descrição atualizada",
        "price": 150.75,
        "stock": 20
    }
    ```

### 5. Excluir Produto
- **Método**: `DELETE`
- **URL**: `/api/products/{id}/delete/`
- **Descrição**: Exclui um produto específico.

---

## **Comentários de Produto**

### 1. Listar Comentários de Produto
- **Método**: `GET`
- **URL**: `/api/products/{id}/comments/`
- **Descrição**: Retorna todos os comentários associados a um produto.
- **Resposta**:
    ```json
    [
        {
            "id": 1,
            "product": 1,
            "author": "João",
            "text": "Ótimo produto!",
            "created_at": "2025-02-13T12:00:00Z",
            "updated_at": "2025-02-13T12:00:00Z",
            "likes": 0,
            "dislikes": 0
        }
    ]
    ```

### 2. Criar Comentário
- **Método**: `POST`
- **URL**: `/api/products/{id}/comments/create/`
- **Descrição**: Cria um novo comentário para um produto específico.
- **Body (JSON)**:
    ```json
    {
        "author": "João",
        "text": "Ótimo produto!"
    }
    ```
- **Resposta**:
    ```json
    {
        "id": 1,
        "product": 1,
        "author": "João",
        "text": "Ótimo produto!",
        "created_at": "2025-02-13T12:00:00Z",
        "updated_at": "2025-02-13T12:00:00Z",
        "likes": 0,
        "dislikes": 0
    }
    ```

### 3. Atualizar Comentário
- **Método**: `PUT`
- **URL**: `/api/comments/{id}/update/`
- **Descrição**: Atualiza um comentário específico.
- **Body (JSON)**:
    ```json
    {
        "author": "João",
        "text": "Comentário atualizado!"
    }
    ```
- **Resposta**:
    ```json
    {
        "id": 1,
        "product": 1,
        "author": "João",
        "text": "Comentário atualizado!",
        "created_at": "2025-02-13T12:00:00Z",
        "updated_at": "2025-02-13T12:30:00Z",
        "likes": 0,
        "dislikes": 0
    }
    ```

### 4. Excluir Comentário
- **Método**: `DELETE`
- **URL**: `/api/comments/{id}/delete/`
- **Descrição**: Exclui um comentário específico.

---

## **Avaliações de Produto**

### 1. Listar Avaliações de Produto
- **Método**: `GET`
- **URL**: `/api/products/{id}/ratings/`
- **Descrição**: Retorna todas as avaliações associadas a um produto.
- **Resposta**:
    ```json
    [
        {
            "id": 1,
            "product": 1,
            "author": "Maria",
            "rating": 5,
            "created_at": "2025-02-13T12:00:00Z"
        }
    ]
    ```

### 2. Criar Avaliação
- **Método**: `POST`
- **URL**: `/api/products/{id}/ratings/create/`
- **Descrição**: Cria uma nova avaliação para um produto específico.
- **Body (JSON)**:
    ```json
    {
        "author": "Maria",
        "rating": 5
    }
    ```
- **Resposta**:
    ```json
    {
        "id": 1,
        "product": 1,
        "author": "Maria",
        "rating": 5,
        "created_at": "2025-02-13T12:00:00Z"
    }
    ```

---

## **Formato das Respostas**

- A resposta de sucesso será sempre no formato JSON.
- Os status de sucesso geralmente têm o código HTTP `200 OK`.
- Quando um recurso é criado com sucesso, o código de resposta será `201 Created`.
- Em caso de erro, o código HTTP será `4xx` ou `5xx` dependendo da natureza do erro (por exemplo, `404 Not Found` ou `400 Bad Request`).

---


