use axum::{Json, extract::State};
use sqlx::PgPool;

use crate::models::{Transaction, NewTransaction};

pub async fn health() -> &'static str {
    "OK"
}

pub async fn get_transactions(
    State(pool): State<PgPool>
) -> Json<Vec<Transaction>> {
    let records = sqlx::query_as!(
        Transaction,
        r#"
        SELECT id, amount, description
        FROM transactions
        ORDER BY id DESC
        LIMIT 10
        "#
    )
    .fetch_all(&pool)
    .await
    .unwrap_or_default();

    Json(records)
}

pub async fn create_transaction(
    State(pool): State<PgPool>,
    Json(payload): Json<NewTransaction>,
) -> Json<Transaction> {
    let record = sqlx::query_as!(
        Transaction,
        r#"
        INSERT INTO transactions (amount, description)
        VALUES ($1, $2)
        RETURNING id, amount, description
        "#,
        payload.amount,
        payload.description
    )
    .fetch_one(&pool)
    .await
    .unwrap();

    Json(record)
}
