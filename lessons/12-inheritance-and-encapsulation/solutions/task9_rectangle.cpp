#include <iostream>

class Rectangle {
public:
    Rectangle(double width, double height) : width(1.0), height(1.0) {
        // Use the setters, so that the starting values are checked too
        set_width(width);
        set_height(height);
    }

    double get_width() const {
        return width;
    }

    double get_height() const {
        return height;
    }

    void set_width(double new_width) {
        if (new_width <= 0) {
            std::cout << "Width must be positive!\n";
            return;
        }
        width = new_width;
    }

    void set_height(double new_height) {
        if (new_height <= 0) {
            std::cout << "Height must be positive!\n";
            return;
        }
        height = new_height;
    }

    double area() const {
        return width * height;
    }

    double perimeter() const {
        return 2 * (width + height);
    }

private:
    double width;
    double height;
};

int main() {
    Rectangle r(3.0, 4.0);
    std::cout << "Width: " << r.get_width() << ", height: " << r.get_height() << "\n";
    std::cout << "Area: " << r.area() << ", perimeter: " << r.perimeter() << "\n";

    r.set_width(10.0);
    std::cout << "New area: " << r.area() << "\n";

    r.set_height(-2.0);  // prints an error message, and leaves the height unchanged
    std::cout << "Height is still: " << r.get_height() << "\n";

    // r.width = 5.0;  // won't compile: `width` is private

    return 0;
}
