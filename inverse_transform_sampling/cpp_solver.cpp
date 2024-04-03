#include <iostream>
#include <fstream>
#include <random>
#include <string>
#include <vector>

class its_solver 
{
public:
    its_solver(double gamma, int size) : gamma(gamma), size(size) {}

    std::vector<double> generate() 
    {
        std::random_device rd;
        std::mt19937 gen(rd());
        std::uniform_real_distribution<> dis(0.1, 0.9);

        std::vector<double> x(size);
        for (int n = 0; n < size; ++n) 
        {
            x[n] = gamma / tan(M_PI * dis(gen));
        }
        return x;
    }

    void save(const std::string& filename, const std::vector<double>& x) 
    {
        std::ofstream file(filename);
        for (const auto& val : x) 
        {
            file << val << "\n";
        }
    }

private:
    double gamma;
    int size;
};

int main(int argc, char* argv[]) 
{
    if (argc != 3) {
        std::cerr << "Usage: " << argv[0] << " gamma size\n";
        return 1;
    }

    double gamma = std::stod(argv[1]);
    int size = std::stoi(argv[2]);

    its_solver solver(gamma, size);
    auto x = solver.generate();
    solver.save("cpp_data.txt", x);

    return 0;
}