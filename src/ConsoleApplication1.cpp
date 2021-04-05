// ConsoleApplication1.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <vector>

class Sign;

class DB 
{
public:
    int con;
    int max_mme_id;
    void set_max_mme_id() {};
    void SplitMultiSign(int id, std::vector<Sign>& signs);
    std::vector<int> get_multi_sign_ids() { std::vector<int>  vi; return vi; };
//    std::vector<Sign> signs;
};

class Sign 
{
public:
    Sign(int root, int id) : root(root), id(id) {}
    int root;
    int id;
    std::string Name;
    int x, y, width, height;
    
    void update_view_box() {}
    void delete_classes() {}
    void save_to_db(DB& db) { db.set_max_mme_id(); };
    void save_to_file() {};

};

void DB::SplitMultiSign(int id, std::vector<Sign>& signs)
{
    int root = 900;
    auto s = new Sign(root, id + 4);
    signs.push_back(*s);
}


int main()
{
    int con;
    DB db;
    
    db.set_max_mme_id();

    std::vector<int> multi_sign_ids = db.get_multi_sign_ids();

    std::vector<Sign> signs;

    for (auto i : multi_sign_ids)
    {
        db.SplitMultiSign(i, signs);
    }

    for (auto sign : signs)
    {
        sign.update_view_box();
        sign.delete_classes();
        sign.save_to_db(db);
        sign.save_to_file();
    }

}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
