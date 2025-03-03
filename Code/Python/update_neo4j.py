from neo4j import GraphDatabase
import os

# Define Neo4j connection details
URI = os.getenv('NEO4J_URL')
USERNAME = os.getenv('NEO4J_USER')
PASSWORD = os.getenv('NEO4J_PASSWORD')

class Neo4jHandler:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def create_nodes_and_relationship(self):
        with self.driver.session() as session:
            session.write_transaction(self._create_nodes)
            session.write_transaction(self._create_relationship)

    @staticmethod
    def _create_nodes(tx):
        tx.run("CREATE (:Person {name: 'Alice'})")
        tx.run("CREATE (:Person {name: 'Bob'})")

    @staticmethod
    def _create_relationship(tx):
        tx.run(
            "MATCH (a:Person {name: 'Alice'}), (b:Person {name: 'Bob'}) "
            "CREATE (a)-[:FRIENDS_WITH]->(b)"
        )


# Run the script
if __name__ == "__main__":
    neo4j_handler = Neo4jHandler(URI, USERNAME, PASSWORD)
    neo4j_handler.create_nodes_and_relationship()
    neo4j_handler.close()
    print("Nodes and relationship created successfully!")