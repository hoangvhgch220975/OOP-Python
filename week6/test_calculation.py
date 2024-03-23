from calculation import calculate_shipping_fee

def test_calculate_shipping_fee():
    weight_unit = 'Kilograms'
    weight = 10
    distance_unit = 'Kilometers'
    distance = 100
    selected_method = 'Standard'
    c = calculate_shipping_fee(weight_unit, weight, distance_unit, distance, selected_method)
    assert c == 11.0  #Expected output

def test_calculate_shipping_fee_2():
    weight_unit = 'Pounds'
    weight = -10
    distance_unit = 'Miles'
    distance = 100
    selected_method = 'Standard'
    c = calculate_shipping_fee(weight_unit, weight, distance_unit, distance, selected_method)
    assert c == 16.0

def test_calculate_shipping_fee_3():
    weight_unit = 'Kilograms'
    weight = 10
    distance_unit = 'Kilometers'
    distance = 100
    selected_method = 'Express'
    c = calculate_shipping_fee(weight_unit, weight, distance_unit, distance, selected_method)
    assert c == 16.0

def test_calculate_shipping_fee_4():
    weight_unit = 'Pounds'
    weight = 10
    distance_unit = 'Miles'
    distance = 100
    selected_method = 'Priority'
    c = calculate_shipping_fee(weight_unit, weight, distance_unit, distance, selected_method)
    assert c == 23.5

def test_calculate_shipping_fee_5():
    weight_unit = 'Kilograms'
    weight = 10
    distance_unit = 'Kilometers'
    distance = 100
    selected_method = 'Priority'
    c = calculate_shipping_fee(weight_unit, weight, distance_unit, distance, selected_method)
    assert c == 36.0

def test_calculate_shipping_fee_6():
    weight_unit = 'Pounds'
    weight = 10
    distance_unit = 'Miles'
    distance = 100
    selected_method = 'Standard'
    c = calculate_shipping_fee(weight_unit, weight, distance_unit, distance, selected_method)
    assert c == 10.0

def test_calculate_shipping_fee_7():
    weight_unit = 'Kilograms'
    weight = 10
    distance_unit = 'Kilometers'
    distance = 100
    selected_method = 'Standard'
    c = calculate_shipping_fee(weight_unit, weight, distance_unit, distance, selected_method)
    assert c == 13.5

def test_calculate_shipping_fee_8():
    weight_unit = 'Pounds'
    weight = 10
    distance_unit = 'Miles'
    distance = 100
    selected_method = 'Express'
    c = calculate_shipping_fee(weight_unit, weight, distance_unit, distance, selected_method)
    assert c == 21.0

def test_calculate_shipping_fee_9():
    weight_unit = 'Kilograms'
    weight = 10
    distance_unit = 'kilometers'
    distance = 100
    selected_method = 'Express'
    c = calculate_shipping_fee(weight_unit, weight, distance_unit, distance, selected_method)
    assert c == 16.0

def test_calculate_shipping_fee_10():
    weight_unit = 'Pounds'
    weight = 10
    distance_unit = 'Miles'
    distance = -100
    selected_method = 'Priority'
    c = calculate_shipping_fee(weight_unit, weight, distance_unit, distance, selected_method)
    assert c == 23.5