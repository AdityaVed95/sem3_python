from bank import Bank


class StateBank(Bank):
    cash = 1500  # class variable of subclass
    print(cash)

    @classmethod
    def available_cash(cls):
        print("Cash in Bank is : ", Bank.cash)
        print("Cash in State Bank is : ", cls.cash)


sb1 = StateBank()
sb1.available_cash()
sb2 = StateBank()
sb1.cash = 2000
print(sb1.cash)
print(sb2.cash)

#
# import java.util. *;
#
# public
#
#
# class Oop1
#     {
#         static
#     int
#     cash = 1000;
#     // the
#     following
#     line
#     will
#     not work as in java
#     we
#     should
#     invoke
#     a
#     function
#     call
#     // within
#     a
#     method
#     only
#     // System.out.println() is a
#     function
#     call \
#     // System.out.println("cash in clas is : ");
#
#     //
#
#     public
#     static
#     void
#     main(String
#     args[])
#     {
#         System.out.println("cash in main is : " + cash);
#     }
#
#     }
