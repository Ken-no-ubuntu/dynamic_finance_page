use serde::{Serialize, Deserialize};

#[derive(Debug, Serialize, Deserialize)]
pub struct Transaction {
    pub id: i32,
    pub amount: f64,
    pub description: String,
}

#[derive(Debug, Deserialize)]
pub struct NewTransaction {
    pub amount: f64,
    pub description: String,
}