from view import QuoteView

if __name__ == '__main__':

    
    quote_view = QuoteView()
    quote_view.create_tables()
    
    # # Add categories
    # try:
    #     quote_view.controller.insert_category("optimistic")
    # except Exception as e:
    #     print(e)
    # try:
    #     quote_view.controller.insert_category("pessimistic")
    # except Exception as e:
    #     print(e)

    # Insert quotes
    # try:
    #     quote_view.insert_quote("The winter is coming", "1984")
    # except Exception as e:
    #     print(e)

    # try:
    #     quote_view.insert_category("neutral")
    # except Exception as e:
    #     print(e)

    # # Assign categories to quotes
    quote_view.controller.assign_category("optimistic", 3)
    quote_view.controller.assign_category("pessimistic", 4)
