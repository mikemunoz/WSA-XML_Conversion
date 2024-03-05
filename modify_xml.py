def modify_xml(file_path):
    """
    Modifies an XML file according to specified rules.
    
    Args:
    file_path (str): Path to the XML file to be modified.
    """
    # Read the content of the original XML file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Prepare a list to store the modified lines
    modified_lines = []
    skip = False

    for line in lines:
        # Skip lines if within the <wccp_service_definition> section
        if '<wccp_service_definition>' in line:
            skip = True
        if '</wccp_config_service_settings>' in line:
            skip = False
            continue

        if skip:
            continue

        # Check for specific patterns and modify the lines accordingly
        if '<radius_cert_type>None</radius_cert_type>' in line:
            modified_lines.append(line)
            modified_lines.append('            <radius_enc_flag>1</radius_enc_flag>\n')
        elif '<cli_radius_cert_type>None</cli_radius_cert_type>' in line:
            modified_lines.append(line)
            modified_lines.append('            <cli_radius_enc_flag>1</cli_radius_enc_flag>\n')
        elif '<password_no_username_resemblance>1</password_no_username_resemblance>' in line:
            modified_lines.append(line)
            modified_lines.append('     <password_no_rep_seq_chars>0</password_no_rep_seq_chars>\n')
        elif '<language>en-us</language>' in line:
            modified_lines.append(line)
            modified_lines.append('      <lock_reason></lock_reason>\n')
        elif '<ise_service_ise_user_timeout>6</ise_service_ise_user_timeout>' in line:
            modified_lines.append(line)
            modified_lines.append('      <ise_service_ers_encind>0</ise_service_ers_encind>\n')
            modified_lines.append('      <ise_service_ise_mem_size>3100</ise_service_ise_mem_size>\n')
            modified_lines.append('      <ise_service_sxp_enabled>0</ise_service_sxp_enabled>\n')
        elif '<log_type>2</log_type>' in line:
            modified_lines.append(line)
            modified_lines.append('    <encr_flag>0</encr_flag>\n')
        elif '<prox_etc_mus_asa_settings_enabled>0</prox_etc_mus_asa_settings_enabled>' in line:
            modified_lines.append(line)
            modified_lines.append('        <prox_etc_mus_asa_settings_enc_pass>1</prox_etc_mus_asa_settings_enc_pass>\n')
        elif '<admin_acl_ip_entry>10.0.0.0/8</admin_acl_ip_entry>' in line:
            continue  # Skip this line
        elif '<amp_thread_pool_limit>125</amp_thread_pool_limit>' in line:
            continue  # Skip this line
        elif '<rep_ssl_enabled>0</rep_ssl_enabled>' in line:
            continue  # Skip this line
        else:
            modified_lines.append(line)  # Keep the line as is if no pattern is matched

    # Write the modified content to a new file
    with open(file_path + '_modified.xml', 'w') as file:
        file.writelines(modified_lines)

# Example usage
modify_xml('exported-filename-here.xml')
