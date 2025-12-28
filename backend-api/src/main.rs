use axum::{
    Router,
    routing::{get, post},
};
use tower_http::cors::CorsLayer;
use dotenvy::dotenv;
use std::net::SocketAddr;

mod handlers;
mod models;
mod database;

#[tokio::main]
async fn main() {
    dotenv().ok();
    tracing_subscriber::fmt::init();

    let db = database::connect().await;

    let cors = CorsLayer::permissive();

    let app = Router::new()
        .route("/health", get(handlers::health))
        .route(
            "/transactions",
            get(handlers::get_transactions)
                .post(handlers::create_transaction),
        )
        .layer(cors)
        .with_state(db);

    let addr = SocketAddr::from(([127, 0, 0, 1], 8080));
    let listener = tokio::net::TcpListener::bind(addr).await.unwrap();

    axum::serve(listener, app).await.unwrap();
}
