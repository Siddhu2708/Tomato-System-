
import streamlit as st
import webbrowser

def Shop():
    st.title ( "🛍️ Tomato Shop" )
    st.write ( "Browse and purchase fertilizers, pesticides, and seeds." )

    general_solutions = [
        {
            'name' : 'Bacterial Speck & Spot Treatment (Agri-mycin)',
            'price' : '₹1588.17',
            'image' : './image/Agri_mycin.jpg',
            'usage' : 'Use Agri-mycin to control bacterial speck and spot. Apply as a foliar spray.',
            'payment_link' : 'https://example.com/payment/Agri-mycin'
        },
        {
            'name' : 'Copper Tank-mixed with Mancozeb',
            'price' : '₹1877.50',
            'image' : './image/Mancozeb.jpg',
            'usage' : 'Copper-based pesticide combined with Mancozeb for controlling various fungal and bacterial diseases.',
            'payment_link' : 'https://example.com/payment/Agri-mycin'
        },
        {
            'name' : 'Damping-Off Treatment (Previcur Flex)',
            'price' : '₹1992.00',
            'image' : './image/Previcur Flex.jpg',
            'usage' : 'Apply Previcur Flex as a directed spray to lower stems and soil for controlling damping-off caused by Pythium.',
            'payment_link' : 'https://example.com/payment/Agri-mycin'
        },
        {
            'name' : 'Damping-Off (Ranman)',
            'price' : '₹2199.50',
            'image' : './image/Ranman.jpg',
            'usage' : 'Apply Ranman as a drench to seeding trays anytime from seeding to 1 week before transplanting for damping-off control.',
            'payment_link' : 'https://example.com/payment/Agri-mycin'
        },
        {
            'name' : 'Gray Mold Control (Botrytis) Treatment',
            'price' : '₹1642.25',
            'image' : './image/Botrytis.jpg',
            'usage' : 'Use fungicides specifically designed for gray mold (Botrytis) control on tomatoes.',
            'payment_link' : 'https://example.com/payment/Agri-mycin'
        },
        {
            'name' : 'Powdery Mildew Treatment (Sulfur-based Fungicide)',
            'price' : '₹1270.90',
            'image' : './image/Sulfur-based Fungicide.jpg',
            'usage' : 'Sulfur-based fungicides to control powdery mildew and other fungal diseases.',
            'payment_link' : 'https://example.com/payment/Agri-mycin'
        },
        {
            'name' : 'Chlorothalonil for Early Blight',
            'price' : '₹1701.50',
            'image' : './image/Chlorothalonil.jpg',
            'usage' : 'Effective for controlling early blight and other fungal diseases like leaf spot caused by Alternaria solani.',
            'payment_link' : 'https://example.com/payment/Agri-mycin'
        },
        {
            'name' : 'Mancozeb for Late Blight',
            'price' : '₹1743.00',
            'image' : './image/Mancozeb2.jpg',
            'usage' : 'Broad-spectrum fungicide that controls late blight, anthracnose, and other fungal diseases in tomatoes.',
            'payment_link' : 'https://example.com/payment/Agri-mycin'
        },
        {
            'name' : 'Copper-based Fungicides for Leaf Spot',
            'price' : '₹1618.50',
            'image' : './image/Copper Fungicides.jpg',
            'usage' : 'Effective against fungal and bacterial diseases like septoria leaf spot and bacterial wilt.',
            'payment_link' : 'https://example.com/payment/Agri-mycin'
        },
        {
            'name' : 'Avid (Acaricide) for Spider Mites',
            'price' : '₹2241.00',
            'image' : './image/Acaricide.jpg',
            'usage' : 'Used to control spider mites, which are common pests on tomato plants.',
            'payment_link' : 'https://example.com/payment/Agri-mycin'
        },
        {
            'name' : 'Onager (Acaricide) for Spider Mites',
            'price' : '₹2407.00',
            'image' : './image/Onager.jpg',
            'usage' : 'Effective for controlling spider mites and other related pests on tomato plants.',
            'payment_link' : 'https://example.com/payment/Agri-mycin'
        },
        {
            'name' : 'Neem Oil for Insect Control',
            'price' : '₹1334.17',
            'image' : './image/Neem Oil.jpg',
            'usage' : 'Organic pesticide effective against aphids, whiteflies, and other insects, as well as fungal infections like powdery mildew.',
            'payment_link' : 'https://example.com/payment/Agri-mycin'
        },
        {
            'name' : 'Cow Dung (Organic Fertilizer)',
            'price' : '₹500.00',
            'image' : './image/Cow Dung.jpg',
            'usage' : 'Use as an organic fertilizer for tomato plants to improve soil health and growth.',
            'payment_link' : 'https://example.com/payment/Agri-mycin'
        },
        {
            'name' : 'Organic Fertilizer',
            'price' : '₹750.00',
            'image' : './image/Organic Fertilizer.jpg',
            'usage' : 'Use as an organic fertilizer to boost tomato plant growth and yield.',
            'payment_link' : 'https://example.com/payment/Agri-mycin'
        },
        {
            'name' : 'Premium Cow Dung Fertilizer',
            'price' : '₹600.00',
            'image' : './image/Premium Cow Dung.jpg',
            'usage' : 'Premium quality cow dung fertilizer for enriching soil, improving plant health, and increasing tomato yields.',
            'payment_link' : 'https://example.com/payment/Agri-mycin'
        }
    ]

    row1_col1, row1_col2, row1_col3 = st.columns ( 3 )
    row2_col1, row2_col2, row2_col3 = st.columns ( 3 )
    row3_col1, row3_col2, row3_col3 = st.columns ( 3 )
    row4_col1, row4_col2, row4_col3 = st.columns ( 3 )
    row5_col1, row5_col2, row5_col3 = st.columns ( 3 )

    with row1_col1 :
        st.image ( general_solutions[0]['image'], width=250 )
        st.write ( f"**{general_solutions[0]['name']}**" )
        st.write ( f"**Price:** {general_solutions[0]['price']}" )
        st.write ( f"**Usage:** {general_solutions[0]['usage']}" )

    with row1_col2 :
        st.image ( general_solutions[1]['image'], width=250 )
        st.write ( f"**{general_solutions[1]['name']}**" )
        st.write ( f"**Price:** {general_solutions[1]['price']}" )
        st.write ( f"**Usage:** {general_solutions[1]['usage']}" )

    with row1_col3 :
        st.image ( general_solutions[2]['image'], width=250 )
        st.write ( f"**{general_solutions[2]['name']}**" )
        st.write ( f"**Price:** {general_solutions[2]['price']}" )
        st.write ( f"**Usage:** {general_solutions[2]['usage']}" )

    with row2_col1 :
        st.image ( general_solutions[3]['image'], width=250 )
        st.write ( f"**{general_solutions[3]['name']}**" )
        st.write ( f"**Price:** {general_solutions[3]['price']}" )
        st.write ( f"**Usage:** {general_solutions[3]['usage']}" )

    with row2_col2 :
        st.image ( general_solutions[4]['image'], width=250 )
        st.write ( f"**{general_solutions[4]['name']}**" )
        st.write ( f"**Price:** {general_solutions[4]['price']}" )
        st.write ( f"**Usage:** {general_solutions[4]['usage']}" )

    with row2_col3 :
        st.image ( general_solutions[5]['image'], width=250 )
        st.write ( f"**{general_solutions[5]['name']}**" )
        st.write ( f"**Price:** {general_solutions[5]['price']}" )
        st.write ( f"**Usage:** {general_solutions[5]['usage']}" )

    with row3_col1 :
        st.image ( general_solutions[6]['image'], width=250 )
        st.write ( f"**{general_solutions[6]['name']}**" )
        st.write ( f"**Price:** {general_solutions[6]['price']}" )
        st.write ( f"**Usage:** {general_solutions[6]['usage']}" )

    with row3_col2 :
        st.image ( general_solutions[7]['image'], width=250 )
        st.write ( f"**{general_solutions[7]['name']}**" )
        st.write ( f"**Price:** {general_solutions[7]['price']}" )
        st.write ( f"**Usage:** {general_solutions[7]['usage']}" )

    with row3_col3 :
        st.image ( general_solutions[8]['image'], width=250 )
        st.write ( f"**{general_solutions[8]['name']}**" )
        st.write ( f"**Price:** {general_solutions[8]['price']}" )
        st.write ( f"**Usage:** {general_solutions[8]['usage']}" )

    with row4_col1 :
        st.image ( general_solutions[9]['image'], width=250 )
        st.write ( f"**{general_solutions[9]['name']}**" )
        st.write ( f"**Price:** {general_solutions[9]['price']}" )
        st.write ( f"**Usage:** {general_solutions[9]['usage']}" )

    with row4_col2 :
        st.image ( general_solutions[10]['image'], width=250 )
        st.write ( f"**{general_solutions[10]['name']}**" )
        st.write ( f"**Price:** {general_solutions[10]['price']}" )
        st.write ( f"**Usage:** {general_solutions[10]['usage']}" )

    with row4_col3 :
        st.image ( general_solutions[11]['image'], width=250 )
        st.write ( f"**{general_solutions[11]['name']}**" )
        st.write ( f"**Price:** {general_solutions[11]['price']}" )
        st.write ( f"**Usage:** {general_solutions[11]['usage']}" )

    with row5_col1 :
        st.image ( general_solutions[12]['image'], width=250 )
        st.write ( f"**{general_solutions[12]['name']}**" )
        st.write ( f"**Price:** {general_solutions[12]['price']}" )
        st.write ( f"**Usage:** {general_solutions[12]['usage']}" )

    with row5_col2 :
        st.image ( general_solutions[13]['image'], width=250 )
        st.write ( f"**{general_solutions[13]['name']}**" )
        st.write ( f"**Price:** {general_solutions[13]['price']}" )
        st.write ( f"**Usage:** {general_solutions[13]['usage']}" )

    with row5_col3 :
        st.image ( general_solutions[14]['image'], width=250 )
        st.write ( f"**{general_solutions[12]['name']}**" )
        st.write ( f"**Price:** {general_solutions[12]['price']}" )
        st.write ( f"**Usage:** {general_solutions[12]['usage']}" )

    # # Initialize session state for cart
    # if "cart" not in st.session_state :
    #     st.session_state.cart = []
    #
    # # Dynamically create rows and columns
    # num_columns = 3
    # columns = st.columns ( num_columns )
    #
    # for idx, product in enumerate ( general_solutions ) :
    #     with columns[idx % num_columns] :
    #         st.image ( product['image'], width=250 )
    #         st.write ( f"**{product['name']}**" )
    #         st.write ( f"**Price:** {product['price']}" )
    #         st.write ( f"**Usage:** {product['usage']}" )
    #
    #         # Create session key for this product
    #         session_key = f"product_{idx}"
    #         if session_key not in st.session_state :
    #             st.session_state[session_key] = False
    #
    #         # Add button to add/remove product from cart
    #         if st.session_state[session_key] :
    #             if st.button ( f"Remove from Cart", key=f"btn_remove_{idx}" ) :
    #                 st.session_state.cart.remove ( product )
    #                 st.session_state[session_key] = False
    #         else :
    #             if st.button ( f"Add to Cart", key=f"btn_add_{idx}" ) :
    #                 st.session_state.cart.append ( product )
    #                 st.session_state[session_key] = True

    # # Show cart summary in sidebar
    # st.sidebar.title ( "🛒 Your Cart" )
    # if st.session_state.cart :
    #     for item in st.session_state.cart :
    #         st.sidebar.write ( f"- {item['name']} ({item['price']})" )
    #     st.sidebar.write ( f"Total Items: {len ( st.session_state.cart )}" )
    #
    #     # Proceed to Payment button
    #     if st.sidebar.button ( "Proceed to Payment" ) :
    #         for item in st.session_state.cart :
    #             # Generate the payment page URL with query parameters
    #             payment_url = f"https://example.com/payment?name={item['name']}&price={item['price']}"
    #             webbrowser.open ( payment_url )
    # else :
    #     st.sidebar.write ( "Your cart is empty." )

