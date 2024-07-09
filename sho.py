#-- shodan.nse
#- Usage: nmap --script shodan <target>

local shodan = require "shodan"

function action()
    local api_key = "YOUR_SHODAN_API_KEY"
    local query = "webcam country:'United States'"
    local results = shodan.search(api_key, query)

    if results and #results > 0 then
        for _, result in ipairs(results) do
            print("IP: " .. result.ip_str)
            print("Port: " .. result.port)
            print("Location: " .. result.location.country_name)
            -- Additional information processing here
        end
    else
        print("No results found.")
    end
end
