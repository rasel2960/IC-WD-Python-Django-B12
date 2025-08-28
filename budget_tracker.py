# budget_tracker.py
import json
import os
import csv
from datetime import datetime

# ANSI color codes for terminal output
COLORS = {
    'info'      : '\033[94m',       # Blue
    'success'   : '\033[92m',       # Green
    'warning'   : '\033[93m',       # Yellow
    'error'     : '\033[91m',       # Red
    'bold'      : '\033[1m',
    'end'       : '\033[0m'
}

def cprint(text, color):
    """Print colored text"""
    print(f"{COLORS.get(color, '')}{text}{COLORS['end']}")

class Transaction:
    def __init__(self, description, amount, category="General"):
        self.description = description
        self.amount = amount  # + for income, - for expense
        self.category = category
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "description": self.description,
            "amount": self.amount,
            "category": self.category,
            "date": self.date
        }

    @property
    def is_income(self):
        return self.amount >= 0


class BudgetTracker:
    def __init__(self, data_file="budget_data.json", backup_file="budget_backup.json"):
        self.data_file = data_file
        self.backup_file = backup_file
        self.transactions = []
        self.monthly_budgets = {}  # category → limit
        self.load_data()

    def add_income(self, desc, amount, category="Income"):
        if amount <= 0:
            cprint("❌ Income must be positive!", "error")
            return
        transaction = Transaction(desc, amount, category)
        self.transactions.append(transaction)
        cprint(f"✅ Added income: ${amount:.2f} from '{desc}'", "success")
        self.save_data()

    def add_expense(self, desc, amount, category="General"):
        if amount <= 0:
            cprint("❌ Expense must be positive!", "error")
            return
        transaction = Transaction(desc, -amount, category)
        self.transactions.append(transaction)
        cprint(f"✅ Expense recorded: -${amount:.2f} for '{desc}'", "success")

        # Warn if near budget limit
        if category in self.monthly_budgets:
            spent = self.get_category_spending(category)
            limit = self.monthly_budgets[category]
            if spent >= 0.8 * limit:
                color = "warning" if spent < limit else "error"
                cprint(f"💸 You've spent ${spent:.2f} of ${limit:.2f} in '{category}' budget!", color)

        self.save_data()

    def set_budget(self, category, amount):
        if amount <= 0:
            cprint("❌ Budget must be positive!", "error")
            return
        self.monthly_budgets[category] = amount
        cprint(f"🎯 Budget set: ${amount:.2f}/month for '{category}'", "success")
        self.save_data()

    def get_balance(self):
        balance = sum(t.amount for t in self.transactions)
        income = sum(t.amount for t in self.transactions if t.is_income)
        expenses = abs(sum(t.amount for t in self.transactions if not t.is_income))
        cprint(f"📊 Current balance: ${balance:.2f}", "info")
        cprint(f"📈 Total income: ${income:.2f} | Total expenses: ${expenses:.2f}", "info")
        return balance

    def get_category_spending(self, category):
        return abs(sum(t.amount for t in self.transactions if not t.is_income and t.category == category))

    def view_spending_by_category(self):
        if not any(not t.is_income for t in self.transactions):
            cprint("📭 No expenses yet.", "info")
            return

        cprint("\n🧾 Spending by Category:", "bold")
        print(f"{'Category':<15} {'Spent':<10} {'Budget':<10} {'Status'}")
        print("-" * 50)

        spent_by_cat = {}
        for t in self.transactions:
            if not t.is_income:
                spent_by_cat[t.category] = spent_by_cat.get(t.category, 0) + abs(t.amount)

        for category, spent in spent_by_cat.items():
            budget = self.monthly_budgets.get(category, 0)
            if budget > 0:
                percent = spent / budget
                if percent >= 1.0:
                    status = "🚨 Over"
                elif percent >= 0.8:
                    status = "⚠️  High"
                else:
                    status = "✅ OK"
            else:
                status = "🔸 No limit"
            print(f"{category:<15} ${spent:<9.2f} ${budget:<9.2f} {status}")

    def list_transactions(self):
        if not self.transactions:
            cprint("📭 No transactions yet.", "info")
            return

        cprint(f"\n📋 All Transactions ({len(self.transactions)})", "bold")
        print(f"{'#':<3} {'Date':<12} {'Type':<6} {'Amount':<10} {'Category':<12} {'Description'}")
        print("-" * 70)
        for i, t in enumerate(self.transactions, 1):
            kind = "INCOME" if t.is_income else "EXPENSE"
            sign = "+" if t.is_income else "-"
            amount = abs(t.amount)
            color = "success" if t.is_income else "warning"
            print(f"{i:<3} {t.date[:10]:<12} {kind:<6} {sign}${amount:<8.2f} {t.category:<12} {t.description}")
        print("-" * 70)

    def export_to_csv(self, filename="budget_export.csv"):
        try:
            with open(filename, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(["Date", "Type", "Amount", "Category", "Description"])
                for t in self.transactions:
                    kind = "Income" if t.is_income else "Expense"
                    amount = abs(t.amount)
                    writer.writerow([t.date, kind, f"{sign}{amount:.2f}", t.category, t.description])
            cprint(f"📁 Data exported to {filename}", "success")
        except Exception as e:
            cprint(f"❌ Failed to export  {e}", "error")

    def save_data(self):
        try:
            # Backup old data
            if os.path.exists(self.data_file):
                os.replace(self.data_file, self.backup_file)

            # Save current data
            data = {
                "transactions": [t.to_dict() for t in self.transactions],
                "monthly_budgets": self.monthly_budgets
            }
            with open(self.data_file, 'w') as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            cprint(f"❌ Error saving  {e}", "error")

    def load_data(self):
        if not os.path.exists(self.data_file):
            cprint("📁 Starting new budget tracker.", "info")
            return

        try:
            with open(self.data_file, 'r') as f:
                data = json.load(f)
                for item in data.get("transactions", []):
                    t = Transaction(
                        item['description'],
                        item['amount'],
                        item['category']
                    )
                    t.date = item['date']
                    self.transactions.append(t)
                self.monthly_budgets = data.get("monthly_budgets", {})
            cprint(f"✅ Loaded {len(self.transactions)} transactions and {len(self.monthly_budgets)} budgets.", "success")
        except Exception as e:
            cprint(f"❌ Failed to load data: {e}", "error")
            cprint("🔁 Attempting to restore from backup...", "warning")
            self.load_backup()

    def load_backup(self):
        try:
            if os.path.exists(self.backup_file):
                with open(self.backup_file, 'r') as f:
                    data = json.load(f)
                    self.transactions = []
                    for item in data.get("transactions", []):
                        t = Transaction(item['description'], item['amount'], item['category'])
                        t.date = item['date']
                        self.transactions.append(t)
                    self.monthly_budgets = data.get("monthly_budgets", {})
                cprint("✅ Restored data from backup.", "success")
            else:
                cprint("❌ No backup available.", "error")
        except Exception as e:
            cprint(f"❌ Backup recovery failed: {e}", "error")


# ——— CLI Interface ———
def main():
    tracker = BudgetTracker()

    commands = """
💰 Budget Tracker Commands:
  add income   <desc> <amount> [category]     - Add income
  add expense  <desc> <amount> [category]     - Add expense
  set budget   <category> <amount>            - Set monthly budget
  balance                                    - View current balance
  report                                     - View spending by category
  history                                    - List all transactions
  export                                     - Export data to CSV
  help                                       - Show this menu
  exit                                       - Save and quit
"""

    cprint(commands, "info")

    while True:
        try:
            cmd = input("\n> ").strip().lower()

            if cmd == "exit":
                cprint("👋 Goodbye! Your data is saved.", "success")
                break

            elif cmd == "help":
                cprint(commands, "info")

            elif cmd == "balance":
                tracker.get_balance()

            elif cmd == "report":
                tracker.view_spending_by_category()

            elif cmd == "history":
                tracker.list_transactions()

            elif cmd == "export":
                tracker.export_to_csv()

            elif cmd.startswith("add income"):
                parts = cmd.split(maxsplit=3)
                if len(parts) < 4:
                    cprint("❌ Usage: add income <desc> <amount> [category]", "error")
                    continue
                try:
                    desc = parts[2]
                    amount = float(parts[3])
                    category = parts[4] if len(parts) > 4 else "Income"
                    tracker.add_income(desc, amount, category)
                except ValueError:
                    cprint("❌ Amount must be a number.", "error")

            elif cmd.startswith("add expense"):
                parts = cmd.split(maxsplit=3)
                if len(parts) < 4:
                    cprint("❌ Usage: add expense <desc> <amount> [category]", "error")
                    continue
                try:
                    desc = parts[2]
                    amount = float(parts[3])
                    category = parts[4] if len(parts) > 4 else "General"
                    tracker.add_expense(desc, amount, category)
                except ValueError:
                    cprint("❌ Amount must be a number.", "error")

            elif cmd.startswith("set budget"):
                parts = cmd.split()
                if len(parts) != 4:
                    cprint("❌ Usage: set budget <category> <amount>", "error")
                    continue
                try:
                    category = parts[2]
                    amount = float(parts[3])
                    tracker.set_budget(category, amount)
                except ValueError:
                    cprint("❌ Amount must be a number.", "error")

            else:
                cprint("❌ Unknown command. Type 'help'.", "error")

        except KeyboardInterrupt:
            cprint("\n\n⚠️  Press 'exit' to quit safely.", "warning")
        except Exception as e:
            cprint(f"💥 Unexpected error: {e}", "error")


if __name__ == "__main__":
    main()