
# This target requires workspace to be properly setup, see readme.
test: 
	cd ../../ \
	&& colcon test --event-handlers console_direct+ \
				--packages-select argus_bot \
	&& colcon test-result

# This target cleans the package.
clean: 
	sudo rm -r install/ build/ log/ 