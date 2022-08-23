public class BagelsOrderItem {
  implements OrderItem {
    double getCost(double price, int quantity) {
      double cost = price * quantity;
      return cost;
    }
    double getPrice() {
      return price;
    }
    int getQuantity() {
      return quantity;
    }
  }
}
