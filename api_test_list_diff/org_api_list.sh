cd /home/emc/Workspaces/VxRailProjects;
find ./ -type f -name "setTestsuitePool_api_*" | xargs grep "loadTestsFromTestCase"
