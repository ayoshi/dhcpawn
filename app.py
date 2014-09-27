from eve import Eve
# import ast

# def post_hosts_post_callback(request, payload):
    # app.data.find('hosts', request, sub_resource_lookup)
    # payload_dict = ast.literal_eval(payload.get_data())
    # host_id = payload_dict['_id']
    # hosts = app.data.driver.db['hosts']
    # host = hosts.find_one({'name': 'my-host217777'})
    # print type(host)
    # print hosts.find_one({'_id': '5403357f23ced7e831c2f455'})
    # print payload_dict['_id']
    
app = Eve()

if __name__ == '__main__':
    # app.on_post_POST_hosts += post_hosts_post_callback
    app.run(debug=True)
