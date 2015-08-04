from testrpc import *

############ Boot ############

evm_reset()

t.set_logging_level(2)
#slogging.configure(':info,eth.pb:debug,eth.vm.exit:trace')
#slogging.configure(':info,eth.vm.exit:debug,eth.pb.tx:info')

print "Ready!"

server = SimpleJSONRPCServer(('localhost', 8545), SimpleJSONRPCRequestHandlerWithCORS)
server.register_function(eth_coinbase, 'eth_coinbase')
server.register_function(eth_accounts, 'eth_accounts')
server.register_function(eth_gasPrice, 'eth_gasPrice')
server.register_function(eth_blockNumber, 'eth_blockNumber')
server.register_function(eth_call, 'eth_call')
server.register_function(eth_sendTransaction, 'eth_sendTransaction')
server.register_function(eth_getCompilers, 'eth_getCompilers')
server.register_function(eth_compileSolidity, 'eth_compileSolidity')
server.register_function(eth_getCode, 'eth_getCode')
server.register_function(eth_getBalance, 'eth_getBalance')
server.register_function(eth_getTransactionCount, 'eth_getTransactionCount')
server.register_function(eth_getTransactionByHash, 'eth_getTransactionByHash')
server.register_function(eth_getTransactionReceipt, 'eth_getTransactionReceipt')
server.register_function(eth_getBlockByNumber, 'eth_getBlockByNumber')
server.register_function(eth_newBlockFilter, 'eth_newBlockFilter')
server.register_function(eth_getFilterChanges, 'eth_getFilterChanges')
server.register_function(eth_uninstallFilter, 'eth_uninstallFilter')
server.register_function(web3_sha3, 'web3_sha3')
server.register_function(web3_clientVersion, 'web3_clientVersion')
server.register_function(evm_reset, 'evm_reset')
server.register_function(evm_snapshot, 'evm_snapshot')
server.register_function(evm_revert, 'evm_revert')
server.serve_forever()
